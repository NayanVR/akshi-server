from utils.openai import client
import ollama

ollama_client = ollama.Client("http://guidelms.in:11434/")

def peform_openai_vision(img_b64: str, prompt: str) -> str:
    messages = [{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img_b64}"
                }
            }
        ]
    }]


    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages, # type: ignore
        max_tokens=300,
        n=1
    )

    return response.choices[0].message.content # type: ignore

def perform_ollama_vision(img_b64: str, prompt: str) -> str:
    response = ollama_client.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [f"{img_b64}"]
        }]
    )

    if response.message.content is None:
        return ""

    return response.message.content
