import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def wetter_als_gedicht(ort="Köln", dichter="Goethe"):
    prompt = (
        f"Wie ist das Wetter heute in {ort}? "
        f"Antworte mit einem kurzen Dreizeiler im Stil von {dichter}."
    )

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=100)

    gedicht = response.choices[0].message.content
    print(gedicht)


if __name__ == '__main__':
    wetter_als_gedicht("Köln", "Friedrich Schiller")
