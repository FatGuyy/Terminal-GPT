from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('GPT_API_KEY')

messages = [
    {"role": "system", "content": "You are a rude abusive assistant."},
]
     

while True:
    message = input("> ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
     
