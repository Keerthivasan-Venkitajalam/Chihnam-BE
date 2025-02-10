import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_audio_file(upload_folder, audio_file):
    """Save uploaded audio file to the designated directory."""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, audio_file.filename)
    audio_file.save(file_path)
    
    logging.info(f"Saved audio file: {file_path}")
    return file_path

def get_timestamp():
    """Return a timestamp string for unique file naming."""
    return datetime.now().strftime("%Y%m%d%H%M%S")

def cleanup_old_files(directory, max_files=50):
    """Remove old files if the directory exceeds max_files."""
    files = sorted(os.listdir(directory), key=lambda f: os.path.getctime(os.path.join(directory, f)))
    
    while len(files) > max_files:
        os.remove(os.path.join(directory, files.pop(0)))
        logging.info(f"Removed old file: {files[0]}")
