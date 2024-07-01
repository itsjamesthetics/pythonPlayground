from vosk import Model, KaldiRecognizer
import os
import wave
import json

def transcribe_audio(audio_file, model_path, transcript_file='transcript.txt'):
    # Load the Vosk model
    model = Model(model_path)
    
    # Open the audio file
    with wave.open(audio_file, "rb") as wf:
        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetMaxAlternatives(0)
        recognizer.SetWords(True)
        
        # Transcribe the audio file
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                pass
        
        # Retrieve the final result
        final_result = json.loads(recognizer.FinalResult())
        
        # Save the transcript
        with open(transcript_file, 'w') as f:
            f.write(final_result.get('text', ''))
        
        print(f"Transcript saved: {transcript_file}")

if __name__ == "__main__":
    model_path = 'path_to_your_vosk_model_directory'  # Update this path
    audio_file = 'temp_audio.wav'  # Update this path
    transcribe_audio(audio_file, model_path)