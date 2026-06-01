"""
YouTube Video Extractor — WAT Tool
Extracts metadata, transcript, and comments from a YouTube video URL.
Uses yt-dlp for metadata, youtube-transcript-api for transcripts,
and YouTube Data API v3 for comments (requires GOOGLE_YOUTUBE_KEY in .env).

Usage:
    python tools/youtube_extract.py <youtube_url> [--lang fr,en] [--max-comments 100]

Output:
    JSON file in tmp/youtube/ with all extracted data.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Load .env
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    for line in env_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, _, value = line.partition('=')
            os.environ.setdefault(key.strip(), value.strip().strip('\'"'))

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'(?:embed/)([a-zA-Z0-9_-]{11})',
        r'(?:shorts/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from: {url}")


def extract_metadata(url: str) -> dict:
    """Extract video metadata using yt-dlp."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        'title': info.get('title'),
        'channel': info.get('channel') or info.get('uploader'),
        'channel_url': info.get('channel_url') or info.get('uploader_url'),
        'upload_date': info.get('upload_date'),
        'duration_seconds': info.get('duration'),
        'duration_string': info.get('duration_string'),
        'view_count': info.get('view_count'),
        'like_count': info.get('like_count'),
        'comment_count': info.get('comment_count'),
        'description': info.get('description'),
        'tags': info.get('tags', []),
        'categories': info.get('categories', []),
        'thumbnail': info.get('thumbnail'),
        'language': info.get('language'),
    }


def extract_transcript(video_id: str, languages: list[str] = None) -> dict:
    """Extract transcript using youtube-transcript-api."""
    if languages is None:
        languages = ['fr', 'en']

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=languages)

        full_text = ' '.join(s.text for s in transcript.snippets)
        segments = [
            {
                'time': round(s.start, 1),
                'duration': round(s.duration, 1),
                'text': s.text,
            }
            for s in transcript.snippets
        ]

        return {
            'status': 'ok',
            'language': transcript.language,
            'full_text': full_text,
            'segments': segments,
            'word_count': len(full_text.split()),
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'full_text': None,
            'segments': [],
        }


def extract_comments_api(video_id: str, max_comments: int = 100, min_length: int = 50) -> list[dict]:
    """Extract top comments using YouTube Data API v3.
    Requires GOOGLE_YOUTUBE_KEY in .env."""
    api_key = os.environ.get('GOOGLE_YOUTUBE_KEY')
    if not api_key:
        print("Warning: GOOGLE_YOUTUBE_KEY not found in .env — skipping comments", file=sys.stderr)
        return []

    try:
        from googleapiclient.discovery import build
        youtube = build('youtube', 'v3', developerKey=api_key)

        comments = []
        next_page = None

        while len(comments) < max_comments:
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                order='relevance',
                maxResults=min(100, max_comments * 3),
                pageToken=next_page,
                textFormat='plainText',
            ).execute()

            for item in response.get('items', []):
                snippet = item['snippet']['topLevelComment']['snippet']
                text = snippet.get('textDisplay', '')
                if len(text) < min_length:
                    continue
                comments.append({
                    'author': snippet.get('authorDisplayName'),
                    'text': text,
                    'likes': snippet.get('likeCount', 0),
                    'is_pinned': False,
                    'published_at': snippet.get('publishedAt'),
                })
                if len(comments) >= max_comments:
                    break

            next_page = response.get('nextPageToken')
            if not next_page:
                break

        comments.sort(key=lambda x: x.get('likes', 0), reverse=True)
        return comments

    except Exception as e:
        print(f"Warning: Could not extract comments via API: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(description='Extract YouTube video data')
    parser.add_argument('url', help='YouTube video URL or ID')
    parser.add_argument('--lang', default='fr,en', help='Transcript languages priority (comma-separated)')
    parser.add_argument('--max-comments', type=int, default=100, help='Max comments to keep (after filtering)')
    parser.add_argument('--min-length', type=int, default=50, help='Min comment length in characters (shorter ones are ignored)')
    parser.add_argument('--no-comments', action='store_true', help='Skip comment extraction (faster)')
    parser.add_argument('--no-transcript', action='store_true', help='Skip transcript extraction')
    args = parser.parse_args()

    languages = [l.strip() for l in args.lang.split(',')]
    video_id = extract_video_id(args.url)
    url = f'https://www.youtube.com/watch?v={video_id}'

    print(f"Extracting: {url}")

    # Extract metadata
    print("  → Metadata...", end=' ', flush=True)
    metadata = extract_metadata(url)
    print(f"OK — {metadata.get('title', 'unknown')}")

    # Extract transcript
    transcript = {'status': 'skipped'}
    if not args.no_transcript:
        print("  → Transcript...", end=' ', flush=True)
        transcript = extract_transcript(video_id, languages)
        if transcript['status'] == 'ok':
            print(f"OK — {transcript['word_count']} words")
        else:
            print(f"Error: {transcript.get('error', 'unknown')}")

    # Extract comments via YouTube API
    comments = []
    if not args.no_comments:
        print(f"  → Comments via API (max {args.max_comments}, min {args.min_length} chars)...", end=' ', flush=True)
        comments = extract_comments_api(video_id, args.max_comments, args.min_length)
        print(f"OK — {len(comments)} comments")

    # Assemble output
    output = {
        'extracted_at': datetime.now().isoformat(),
        'video_id': video_id,
        'url': url,
        'metadata': metadata,
        'transcript': transcript,
        'comments': comments,
    }

    # Save to tmp/youtube/
    output_dir = Path(__file__).parent.parent / 'tmp' / 'youtube'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Filename from title or video ID
    safe_title = re.sub(r'[^\w\s-]', '', metadata.get('title', video_id) or video_id)
    safe_title = re.sub(r'\s+', '_', safe_title)[:80]
    output_path = output_dir / f"{safe_title}.json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n  Saved: {output_path}")
    return str(output_path)


if __name__ == '__main__':
    main()
