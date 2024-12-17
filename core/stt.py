from fastapi import HTTPException
from utils.openai import client
import io

def speech_to_text(audio_data: bytes) -> str:
    try:
        audio_file = io.BytesIO(audio_data)
        audio_file.name = "audio.wav"

        return client.audio.transcriptions.create(
            model="whisper-1",
            language="en",
            response_format="text",
            file=audio_file
        )
    except Exception as e:
        print(f"Error in speech to text: {str(e)}")
        raise HTTPException(status_code=500, detail="Error in speech to text")
