# Akshi Server

Akshi Server is a FastAPI-based application that provides functionalities for speech-to-text (STT), text-to-speech (TTS), and image processing using OpenAI's models. This server allows users to upload an image and an audio file, process the audio to generate a text prompt, analyze the image based on the prompt, and convert the resulting text back to speech.

## Installation

### Prerequisites

- [uv](https://docs.astral.sh/uv/) - A universal virtualenv manager for dependency isolation and management
- OpenAI API Key

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/akshi-server.git
    cd akshi-server
    ```

2. Create a virtual environment and install dependencies:

    ```sh
    uv sync
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the server:

    ```sh
    uv run fastapi run main.py
    ```

    The server should now be running at `http://localhost:8000`.
    You can access the API documentation at `http://localhost:8000/docs`.

### Note

To manage packages, use the `uv` command followed by the desired action.

For example, to install a new package:

```sh
uv add xyz_package
```

To remove a package:
```sh
uv remove
```

To run a command in the virtual environment:
```sh
uv run python script.py
```
