import ollama

response = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "Tell me an interesting fact about Snakes",
        },
    ],
)

print(response["message"]["content"])