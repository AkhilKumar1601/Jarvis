import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_news():
    url = url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch news."

    data = response.json()

    headlines = []

    for article in data["articles"][0:5]:
        headlines.append(article["title"])

    return "\n\n".join(headlines)
