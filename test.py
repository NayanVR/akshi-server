import ollama

ollama_client = ollama.Client("http://guidelms.in:11434/")

response = ollama_client.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': "How are you?",
    }]
)

print(response.message.content)
