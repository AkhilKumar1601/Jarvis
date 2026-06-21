# 🤖 Jarvis AI Assistant

A modular AI-powered virtual assistant built with Python for learning and exploring the fundamentals of Artificial Intelligence, APIs, and software architecture.

Jarvis can open websites, play music, fetch live news, and answer general questions using Google's Gemini API. The project focuses on clean code, modular design, and building strong Python foundations for AI/ML.

---

## ✨ Features

- 🗣️ Wake-word based interaction
- 🌐 Open frequently used websites
- 🎵 Play songs from a custom music library
- 📰 Fetch latest headlines using NewsAPI
- 🧠 Gemini AI integration for general conversations
- 😴 Sleep mode
- 📂 Modular and maintainable architecture
- ⚡ Fallback to AI when no predefined command matches

---

## 🏗️ Project Structure

```
Jarvis/
│
├── main.py                 # Main application
├── gpt_client.py           # Gemini API integration
├── news.py                 # News fetching functionality
├── music_library.py        # Song library
├── website_library.py      # Website shortcuts
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Technologies Used

- Python 3
- Google Gemini API
- NewsAPI
- Requests
- python-dotenv
- Webbrowser module
- Virtual Environments

---

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/<your-username>/Jarvis.git
cd Jarvis
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

#### Linux / WSL

```bash
source env/bin/activate
```

#### Windows

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
```

---

## ▶️ Run Jarvis

```bash
python main.py
```

---

## Example Interaction

```
You: jarvis
Jarvis: I am here.

You: hello
Jarvis: Hello, Akhil.

You: open google
Jarvis: Opening google

You: latest news
Jarvis: 1. ...

You: what is machine learning?
Jarvis: Machine Learning is a subset of AI...
```

---

## 📚 Concepts Practiced

This project was built primarily for learning and strengthening:

- Functions and Modules
- Dictionaries and Lists
- Error Handling
- APIs and JSON
- Environment Variables
- Virtual Environments
- Clean Code and Project Structure
- AI Integration with LLMs
- Python Fundamentals for AI/ML

---

## 🎯 Purpose

This project is part of my journey into Artificial Intelligence and Machine Learning. The goal is to build strong Python fundamentals through practical projects and gradually progress toward advanced AI systems.

---

## ⭐ If you found this project useful, consider giving it a star!
