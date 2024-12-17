from fastapi import HTTPException
from utils.openai import client

def text_to_speech(text: str) -> bytes:
    try:
        return client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=text,
            response_format="mp3",
        ).content
    except Exception as e:
        print(f"Error in text to speech: {str(e)}")
        raise HTTPException(status_code=500, detail="Error in text to speech")
