from fastapi import APIRouter, HTTPException, UploadFile
import base64

from core.stt import speech_to_text
from core.vision import peform_vision
from core.tts import text_to_speech
from utils.storage import save_audio_file


router = APIRouter()

@router.post("/process-scene")
async def process_scene(image: UploadFile, audio: UploadFile):
    try:
        audio_data = await audio.read()
        image_data = await image.read()

        prompt = speech_to_text(audio_data)
        image_base64 = base64.b64encode(image_data).decode("utf-8")

        scene_response = peform_vision(image_base64, prompt)

        audio_output = text_to_speech(scene_response)
        audio_output_path = save_audio_file(audio_output)

        return audio_output_path

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
