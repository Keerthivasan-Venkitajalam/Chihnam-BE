from gtts import gTTS
from TTS.api import TTS
import os

OUTPUT_TTS_PATH = "static/tts_output/"

# Ensure the output directory exists
os.makedirs(OUTPUT_TTS_PATH, exist_ok=True)

def synthesize_gtts(text, output_file="gtts_output.mp3"):
    """Convert text to speech using Google TTS and save it as an MP3 file."""
    output_path = os.path.join(OUTPUT_TTS_PATH, output_file)
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    return output_path

# Load Coqui TTS model once (for efficiency)
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def synthesize_coqui(text, output_file="coqui_output.wav"):
    """Convert text to speech using Coqui TTS and save it as a WAV file."""
    output_path = os.path.join(OUTPUT_TTS_PATH, output_file)
    tts_model.tts_to_file(text=text, file_path=output_path)
    return output_path
