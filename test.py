import openai

openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
     

while True:
    message = input("User : ")
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