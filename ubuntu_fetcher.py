import os
import requests
from urllib.parse import urlparse
from datetime import datetime
import hashlib

def sanitize_filename(url):
    """
    Generate a safe filename from a URL or timestamp.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If no filename, generate one
    if not filename:
        filename = "image_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    return filename

def get_file_hash(content):
    """
    Generate a hash for the file content to detect duplicates.
    """
    return hashlib.sha256(content).hexdigest()

def fetch_images(urls):
    """
    Download images from a list of URLs and save them locally.
    """
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Track already downloaded file hashes to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        try:
            print(f"Fetching {url} ...")
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Precaution: check headers before saving
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                print(f"Skipped {url} (not an image, content-type: {content_type})")
                continue

            # Generate filename
            filename = sanitize_filename(url)
            filepath = os.path.join(save_dir, filename)

            # Compute hash to avoid duplicates
            file_content = response.content
            file_hash = get_file_hash(file_content)

            if file_hash in downloaded_hashes:
                print(f"Skipped {url} (duplicate image detected)")
                continue

            # Save image
            with open(filepath, "wb") as f:
                f.write(file_content)

            downloaded_hashes.add(file_hash)
            print(f"Saved as {filepath}")

        except requests.exceptions.RequestException as e:
            print(f" Error fetching {url}: {e}")

if __name__ == "__main__":
    # Prompt user for multiple URLs (comma-separated)
    url_input = input("Enter image URLs (separated by commas): ").strip()
    urls = [u.strip() for u in url_input.split(",") if u.strip()]
    fetch_images(urls)
