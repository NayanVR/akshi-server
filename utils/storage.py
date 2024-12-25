import os
from uuid import uuid4


def save_audio_file(file: bytes) -> str:
    dir_name = "static"
    file_id = uuid4().hex

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    file_path = os.path.join(dir_name, f"{file_id}.wav")
    with open(file_path, "wb") as f:
        f.write(file)

    return file_path
