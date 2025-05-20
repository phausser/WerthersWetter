import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def wetter_als_gedicht(wetter, ort="Köln", dichter="Goethe"):
    prompt = (
        f"Das Wetter heute in {ort} ist {wetter}"
        f"Beschreibe es mit einem kurzen Dreizeiler im Stil von {dichter}. Erwähne die Temperatur."
    )

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=100)

    gedicht = response.choices[0].message.content
    return f"{gedicht}\/n({dichter})"


def get_weather(location):
    url = f"https://wttr.in/{location}?format=%C+%t"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Fehler beim Abrufen der Wetterdaten: {e}"


if __name__ == '__main__':
    weather = get_weather("cologne")
    print(wetter_als_gedicht(weather, "Köln", "Goethe"))
