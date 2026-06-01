"""
Render HTML/CSS slides to PNG images via HCTI (htmlcsstoimage.com) API.

Usage:
    python tools/render_hcti.py <directory_or_html_file> [--width 1080] [--height 1350]

Arguments:
    directory_or_html_file  Path to a directory of slide-*.html files, or a single .html file.
    --width                 Viewport width in pixels (default: 1080).
    --height                Viewport height in pixels (default: 1350).

Processes each HTML file, sends it to HCTI API, downloads the resulting PNG.
Output PNGs are saved next to the HTML files with the same name.

Requires HCTI_USER_ID and HCTI_API_KEY in .env at project root.
"""

import os
import re
import sys
import glob
import time
import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(PROJECT_ROOT, ".env")

HCTI_API_URL = "https://hcti.io/v1/image"


def load_credentials():
    """Load HCTI_USER_ID and HCTI_API_KEY from .env file."""
    if not os.path.exists(ENV_PATH):
        print(f"ERROR: .env not found at {ENV_PATH}")
        sys.exit(1)

    creds = {}
    with open(ENV_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("HCTI_USER_ID="):
                creds["user_id"] = line.split("=", 1)[1].strip("\"'")
            elif line.startswith("HCTI_API_KEY="):
                creds["api_key"] = line.split("=", 1)[1].strip("\"'")

    if "user_id" not in creds or "api_key" not in creds:
        print("ERROR: HCTI_USER_ID and/or HCTI_API_KEY not found in .env")
        print("Get your credentials at https://htmlcsstoimage.com/dashboard")
        sys.exit(1)

    return creds["user_id"], creds["api_key"]


def extract_html_css(filepath):
    """Read an HTML file and split into body HTML and CSS content."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract CSS from <style> tags (handles attributes like <style type="text/css">)
    css_parts = re.findall(r"<style[^>]*>(.*?)</style>", content, re.DOTALL)
    css = "\n".join(part.strip() for part in css_parts)

    # Remove @import lines from CSS — fonts are loaded via google_fonts API param
    css = re.sub(r"@import\s+url\([^)]+\)\s*;?\s*", "", css)

    # Extract body content
    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL)
    html = body_match.group(1).strip() if body_match else content

    return html, css


def render_slide(user_id, api_key, html, css, width, height, retries=3):
    """Send HTML/CSS to HCTI API and return the image URL. Retries on failure."""
    payload = {
        "html": html,
        "css": css,
        "google_fonts": "Oswald:400,600,700|Poppins:300,400,600",
        "viewport_width": width,
        "viewport_height": height,
        "device_scale": 1,
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(
                HCTI_API_URL,
                auth=(user_id, api_key),
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()

            image_url = result.get("url")
            if not image_url:
                print(f"  ERROR: No URL in response: {result}")
                return None
            return image_url

        except requests.exceptions.HTTPError:
            print(f"  ERROR: API returned {response.status_code}: {response.text}")
        except Exception as e:
            print(f"  ERROR: {e}")

        if attempt < retries:
            wait = attempt * 2
            print(f"  Retrying in {wait}s (attempt {attempt + 1}/{retries})...")
            time.sleep(wait)

    return None


def download_image(url, output_path):
    """Download image from URL and save to disk."""
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(resp.content)
        return True
    except Exception as e:
        print(f"  ERROR downloading: {e}")
        return False


def process_files(html_files, width, height):
    """Process a list of HTML files through the HCTI API."""
    user_id, api_key = load_credentials()

    total = len(html_files)
    success = 0

    print(f"Rendering {total} slide(s) via HCTI API ({width}x{height}px)...\n")

    for i, html_file in enumerate(html_files, 1):
        basename = os.path.splitext(os.path.basename(html_file))[0]
        output_path = os.path.join(os.path.dirname(html_file), f"{basename}.png")

        print(f"[{i}/{total}] {basename}")

        html, css = extract_html_css(html_file)
        image_url = render_slide(user_id, api_key, html, css, width, height)

        if not image_url:
            print(f"  FAILED\n")
            continue

        if download_image(image_url, output_path):
            print(f"  OK -> {output_path}\n")
            success += 1
        else:
            print(f"  FAILED to download\n")

    print(f"Done: {success}/{total} slides rendered.")
    return success


def run():
    if len(sys.argv) < 2:
        print("Usage: python tools/render_hcti.py <directory_or_html_file> [--width 1080] [--height 1350]")
        sys.exit(1)

    target = sys.argv[1]
    width = 1080
    height = 1350

    # Parse optional args
    args = sys.argv[2:]
    for i, arg in enumerate(args):
        if arg == "--width" and i + 1 < len(args):
            width = int(args[i + 1])
        elif arg == "--height" and i + 1 < len(args):
            height = int(args[i + 1])

    # Determine HTML files to process
    if os.path.isdir(target):
        html_files = sorted(glob.glob(os.path.join(target, "slide-*.html")))
        if not html_files:
            print(f"ERROR: No slide-*.html files found in {target}")
            sys.exit(1)
    elif os.path.isfile(target) and target.endswith(".html"):
        html_files = [target]
    else:
        print(f"ERROR: {target} is not a valid directory or HTML file")
        sys.exit(1)

    success = process_files(html_files, width, height)
    if success < len(html_files):
        sys.exit(1)


if __name__ == "__main__":
    run()
