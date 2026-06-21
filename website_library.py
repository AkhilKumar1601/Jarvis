import webbrowser

websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://github.com",
    "twitter": "https://x.com",
    "x": "https://x.com",
    "excalidraw": "https://excalidraw.com",
    "notion": "https://www.notion.so",
    "chatgpt": "https://chatgpt.com",
    "gemini": "https://gemini.google.com",
    "claude": "https://claude.ai"
}

def open_website(website):
  webbrowser.open(websites[website])
  return f"Opening {website}"