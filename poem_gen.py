from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def poem_generator(topic, poetry_type="free verse"):

    completions = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer",
                "content": "You are a creative writer"
            },
            {
                "role": "user",
                "content": f"Write a {poetry_type} poetry about {topic}"
            }
        ]
    )

    return completions.choices[0].message.content


