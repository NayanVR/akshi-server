import os

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, WebSocketException
import aiofiles

from utils.constants import UPLOAD_DIR

router = APIRouter()

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.websocket("/ws/scene")
async def process_scene(websocket: WebSocket):
    await websocket.accept()

    uploaded_files: dict[str, str | None] = {"audio": None, "image": None}
    try:
        while True:
            file_type = await websocket.receive_text()

            if file_type in ["audio", "image"]:
                data = await websocket.receive_bytes()
                file_extension = "wav" if file_type == "audio" else "jpg"
                file_name = f"{file_type}_received.{file_extension}"
                save_path = os.path.join(UPLOAD_DIR, file_name)

                async with aiofiles.open(save_path, "wb") as file:
                    await file.write(data)

                uploaded_files[file_type] = save_path
                await websocket.send_text(f"{file_type.capitalize()} file saved as {file_name}")

                # Check if both files are uploaded
                if all(uploaded_files.values()):
                    # response_message = await process_files(uploaded_files["audio"], uploaded_files["image"])
                    # await websocket.send_text(response_message)

                    uploaded_files = {"audio": None, "image": None}

    except (WebSocketDisconnect, WebSocketException):
        await websocket.close()
    except Exception as e:
        print(f"Error in process_scene: {str(e)}")
        await websocket.close()
