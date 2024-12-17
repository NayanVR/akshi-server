from utils.openai import client

def peform_vision(img_b64: str, prompt: str) -> str:
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
