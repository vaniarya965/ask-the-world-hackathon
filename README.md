# 🗣️ Ask the World — A Voice-First Assistant for the Visually Impaired

**Built for the SerpApi India Hackathon 2026**

> "The world is full of answers. Not everyone can read them off a screen."

## 💡 The Problem

Over 250 million people worldwide live with visual impairment. For them, a simple question like *"Is there a pharmacy nearby that's still open?"* or *"What's happening in the news today?"* isn't a quick Google search — it means depending on someone else, or on expensive, purpose-built assistive hardware that most people can't afford.

Information is everywhere. Access to it, hands-free and screen-free, isn't.

## 🎯 The Idea

**Ask the World** is a voice-first assistant that answers real, live questions out loud — no screen, no typing, no waiting on someone else. You speak a question. It listens, searches the real web using SerpApi, and speaks back a clear, direct answer.

## 🦯 Why I Built This

This builds on an ongoing project of mine: an **AI-powered smart cane** for visually impaired users — a low-cost cane fitted with a camera and voice agent that describes surroundings through an earpiece, designed as an affordable alternative to expensive commercial solutions. The cane tells you what's *physically* around you. Ask the World tells you what you *ask* for, pulling from the entire web.

## ⚙️ How It Works

1. **Listen** — records audio from the microphone
2. **Understand** — converts speech to text
3. **Route intelligently** — "near me" style questions go to SerpApi's Google Local API; general questions go to Google Search API
4. **Speak** — reads the top result aloud

## 🛠️ Tech Stack

- Python
- SerpApi (Google Local API + Google Search API)
- SpeechRecognition + sounddevice (voice input)
- pyttsx3 (voice output)

## 🚀 Running It

```bash
pip install requests pyttsx3 sounddevice speechrecognition# 🗣️ Ask the World — A Voice-First Assistant for the Visually Impaired

**Built for the SerpApi India Hackathon 2026**

> "The world is full of answers. Not everyone can read them off a screen."

## 💡 The Problem

Over 250 million people worldwide live with visual impairment. For them, a simple question like *"Is there a pharmacy nearby that's still open?"* or *"What's happening in the news today?"* isn't a quick Google search — it means depending on someone else, or on expensive, purpose-built assistive hardware that most people can't afford.

Information is everywhere. Access to it, hands-free and screen-free, isn't.

## 🎯 The Idea

**Ask the World** is a voice-first assistant that answers real, live questions out loud — no screen, no typing, no waiting on someone else. You speak a question. It listens, searches the real web using SerpApi, and speaks back a clear, direct answer.

## 🦯 Why I Built This

This builds on an ongoing project of mine: an **AI-powered smart cane** for visually impaired users — a low-cost cane fitted with a camera and voice agent that describes surroundings through an earpiece, designed as an affordable alternative to expensive commercial solutions. The cane tells you what's *physically* around you. Ask the World tells you what you *ask* for, pulling from the entire web.

## ⚙️ How It Works

1. **Listen** — records audio from the microphone
2. **Understand** — converts speech to text
3. **Route intelligently** — "near me" style questions go to SerpApi's Google Local API; general questions go to Google Search API
4. **Speak** — reads the top result aloud

## 🛠️ Tech Stack

- Python
- SerpApi (Google Local API + Google Search API)
- SpeechRecognition + sounddevice (voice input)
- pyttsx3 (voice output)

## 🚀 Running It

```bash
pip install requests pyttsx3 sounddevice speechrecognition