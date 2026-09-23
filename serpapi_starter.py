
import requests
import pyttsx3 
import sounddevice as sd
import wave
import speech_recognition as sr 

import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("SERPAPI_KEY") 

def search_nearby(query, location="Mumbai, Maharashtra, India"):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_local",
        "q": query,
        "location": location,
        "api_key": API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data.get("local_results", [])
    if not results:
        print("No results found. Check your API key or try a different query.")
        return []
    print(f"\nTop results for '{query}' near {location}:\n")
    for i, place in enumerate(results[:5], start=1):
        name = place.get("title", "Unknown name")
        address = place.get("address", "No address listed")
        hours = place.get("hours", "Hours not listed")
        print(f"{i}. {name}")
        print(f"   Address: {address}")
        print(f"   Hours: {hours}\n")
    return results


def search_general(query):
    url = "https://serpapi.com/search"
    params = {"engine": "google", "q": query, "api_key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    answer_box = data.get("answer_box", {})
    if answer_box:
        answer = answer_box.get("answer") or answer_box.get("snippet")
        if answer:
            print(f"\nDirect answer for '{query}':\n{answer}\n")
            return answer
    organic_results = data.get("organic_results", [])
    if not organic_results:
        print("No results found. Check your API key or try a different query.")
        return None
    top = organic_results[0]
    print(f"\nTop result for '{query}':\n{top.get('title')}\n{top.get('snippet')}\n")
    return top.get("snippet")


LOCAL_TRIGGER_WORDS = ["near me", "nearby", "open now", "closest", "nearest"]

def route_query(query):
    lowered = query.lower()
    if any(trigger in lowered for trigger in LOCAL_TRIGGER_WORDS):
        print(f"(Routing '{query}' -> local/places search)")
        return search_nearby(query)
    else:
        print(f"(Routing '{query}' -> general search)")
        return search_general(query) 
def speak(text):
    """Reads the given text out loud."""
    if not text:
        print("(Nothing to speak)")
        return
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 

def listen():
    """Records a few seconds of audio from the mic and converts it to text."""
    duration = 4
    samplerate = 44100

    print("Listening... speak now")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    filename = "voice_input.wav"
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes()) 

    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Speech recognition service error.")
        return None
spoken_query = listen()
if spoken_query:
        result = route_query(spoken_query)
        if isinstance(result, list) and result:
            first = result[0]
            speak(f"The nearest result is {first.get('title')}, {first.get('hours', '')}")
        elif isinstance(result, str):
            speak(result)