import whisper
import torch
import librosa
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Load Whisper model
whisper_model = whisper.load_model("base")

# Load Wav2Vec2 model
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
w2v_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def transcribe_whisper(audio_path):
    """Transcribe audio using Whisper ASR model."""
    result = whisper_model.transcribe(audio_path)
    return result["text"]

def transcribe_wav2vec2(audio_path):
    """Transcribe audio using Wav2Vec2 ASR model."""
    y, sr = librosa.load(audio_path, sr=16000)
    inputs = processor(y, sampling_rate=sr, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = w2v_model(inputs.input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    
    return transcription
