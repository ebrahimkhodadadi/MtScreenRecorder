import glob
import os
import time
        
def find_mkv_file():
    """Find the first .mkv file in the current directory."""
    mkv_files = glob.glob("*.mkv")
    if mkv_files:
        return mkv_files[0]  # Return the first .mkv file found
    else:
        return None
    
def delete_files_with_retry(*filenames, retries=5, delay=1):
    """Tries to delete multiple files, retrying if they are in use."""
    for file in filenames:
        for attempt in range(retries):
            if os.path.exists(file):
                try:
                    os.remove(file)
                    print(f"🗑️ Deleted: {file}")
                    break  # Exit loop if deletion is successful
                except Exception as e:
                    print(f"⚠️ Attempt {attempt + 1}: Failed to delete {file}, retrying... ({e})")
                    time.sleep(delay)  # Wait before retrying
            else:
                print(f"⚠️ File not found: {file}")
                break  # No need to retry if file doesn't exist
