"""
Fetch stock images from Unsplash and download them to a local directory.

Usage:
    python tools/fetch_stock_images.py --query "paris apartment interior" --count 5 --out tmp/carousel/{slug}/images/

Arguments:
    --query     Search keywords for Unsplash
    --count     Number of images to fetch (default: 5, max: 10)
    --out       Output directory path (created if missing)
    --orient    Photo orientation: portrait, landscape, squarish (default: portrait)

Requires UNSPLASH_ACCESS_KEY in .env at the carousel skill root.
"""

import os
import sys
import argparse
import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(PROJECT_ROOT, ".env")

UNSPLASH_SEARCH_URL = "https://api.unsplash.com/search/photos"


def load_env(path):
    env = {}
    if not os.path.exists(path):
        return env
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            env[key.strip()] = val.strip()
    return env


def search_unsplash(query, count, orientation, access_key):
    params = {
        "query": query,
        "orientation": orientation,
        "per_page": min(count, 10),
    }
    headers = {"Authorization": f"Client-ID {access_key}"}
    resp = requests.get(UNSPLASH_SEARCH_URL, params=params, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("results", [])


def download_image(photo, out_dir, index):
    raw_url = photo["urls"]["raw"]
    download_url = f"{raw_url}&w=1080&q=80&fm=jpg&fit=crop"
    photo_id = photo["id"]
    author = photo["user"]["username"]
    filename = f"stock-{index:02d}-{photo_id}.jpg"
    dest = os.path.join(out_dir, filename)

    resp = requests.get(download_url, timeout=30, stream=True)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

    size_kb = os.path.getsize(dest) // 1024
    return dest, author, size_kb


def main():
    parser = argparse.ArgumentParser(description="Fetch Unsplash stock images")
    parser.add_argument("--query", required=True, help="Search keywords")
    parser.add_argument("--count", type=int, default=5, help="Number of images (max 10)")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--orient", default="portrait", choices=["portrait", "landscape", "squarish"])
    args = parser.parse_args()

    env = load_env(ENV_PATH)
    access_key = env.get("UNSPLASH_ACCESS_KEY", "")
    if not access_key:
        print(f"ERROR: UNSPLASH_ACCESS_KEY not found in {ENV_PATH}", file=sys.stderr)
        sys.exit(1)

    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)

    print(f"Searching Unsplash: \"{args.query}\" ({args.count} images, {args.orient})")
    results = search_unsplash(args.query, args.count, args.orient, access_key)

    if not results:
        print("No results found. Try different keywords.")
        sys.exit(0)

    print(f"Found {len(results)} photos — downloading to {out_dir}\n")

    downloaded = []
    for i, photo in enumerate(results, 1):
        try:
            path, author, size_kb = download_image(photo, out_dir, i)
            downloaded.append(path)
            print(f"  [{i}] {os.path.basename(path)} ({size_kb} KB) — @{author}")
        except Exception as e:
            print(f"  [{i}] ERREUR: {e}", file=sys.stderr)

    print(f"\n{len(downloaded)}/{len(results)} images téléchargées dans {out_dir}")

    for path in downloaded:
        print(f"  {path}")


if __name__ == "__main__":
    main()
