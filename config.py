import os

# Flask Configuration
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000

# Directories
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads/audio")
SPECTROGRAM_FOLDER = os.path.join(BASE_DIR, "static/spectrograms")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Whisper Model Path
WHISPER_MODEL_SIZE = "base"  # Can be "tiny", "small", "medium", "large"
WHISPER_MODEL_PATH = os.path.join(MODEL_DIR, "whisper")

# TTS Model Path
COQUI_TTS_MODEL = "tts_models/en/ljspeech/tacotron2-DDC"

# Google TTS Settings
DEFAULT_TTS_ENGINE = "gtts"  # Options: "gtts", "coqui"

# API Keys (if needed)
NGROK_AUTH_TOKEN = "2mVh8DPGJzUIMrTRuq1bS5sTw0X_4c3LwbYcvct82xfz2gpSc"  # Replace with actual ngrok token
