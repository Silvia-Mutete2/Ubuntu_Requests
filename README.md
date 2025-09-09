# Ubuntu_Requests

**The Wisdom of Ubuntu: "I am because we are"**

This project is an **Ubuntu-inspired Image Fetcher** built in Python.  
It allows you to fetch images from the web respectfully, organize them locally, and avoid duplicates — honoring the Ubuntu principles of **community, respect, sharing, and practicality**.

---

##  Features
-  Fetch one or multiple images from URLs  
-  Saves all images into a folder called `Fetched_Images`  
-  Automatically creates the folder if it doesn’t exist  
-  Extracts filenames from URLs (or generates one if missing)  
-  Prevents duplicate downloads using file hashing  
-  Checks HTTP headers to confirm the resource is an image  
-  Handles errors gracefully without crashing  

---

##  Requirements
- Python 3.x  
- `requests` library  

Install dependencies:
```bash
pip install requests

