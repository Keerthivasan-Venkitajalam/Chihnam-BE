import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

SPECTROGRAM_PATH = "static/spectrograms/latest_spectrogram.png"

def generate_spectrogram(audio_path):
    """Generates and saves a spectrogram from an audio file."""
    y, sr = librosa.load(audio_path, sr=16000)  # Load audio
    S = librosa.feature.melspectrogram(y=y, sr=sr)  # Compute mel spectrogram
    S_db = librosa.power_to_db(S, ref=np.max)  # Convert to dB scale

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    plt.tight_layout()
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(SPECTROGRAM_PATH), exist_ok=True)
    
    plt.savefig(SPECTROGRAM_PATH)
    plt.close()
    
    return SPECTROGRAM_PATH
