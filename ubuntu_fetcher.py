import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # Prompt user for URL
    url = input("Enter the image URL: ").strip()

    # Create directory if not exists
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise error for bad status

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename:
            filename = "image_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

        # Full path to save
        filepath = os.path.join(save_dir, filename)

        # Save in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Image saved successfully as {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")

if __name__ == "__main__":
    fetch_image()
