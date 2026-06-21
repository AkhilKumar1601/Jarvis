from website_library import websites,open_website
from music_library import songs,play_song
from news import get_news
from gpt_client import ask_gpt
# import speech_recognition as sr
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

def take_command():
  return input("You: ")
    # try:
    #     with sr.Microphone() as source:
    #       print("Listening")
    #       recognizer.adjust_for_ambient_noise(source)
    #       audio = recognizer.listen(
    #         source,
    #         timeout=5,
    #         phrase_time_limit=10
    #       )
    #       command = recognizer.recognize_google(audio)
    #       print(f"You: {command}")
    #       return command

    # except sr.UnknownValueError:
    #     return ""

    # except sr.RequestError:
    #     return ""

    # except Exception:
    #     return ""

def speak(response):
 print(f"Jarvis: {response}\n")
#  engine.say(response)
#  engine.runAndWait()

def process_command(command):
 cmd = command.lower()

 if "hello" in cmd:
  return "Hello, Akhil."

 elif "how are you" in cmd:
  return "I am doing great."

 elif "who are you" in cmd:
  return "I am jarvis your virtual assistant"

 elif "news" in cmd:
  return get_news()

 for song in songs:
   if song in cmd:
     return play_song(song)

 for website in websites:
   if website in cmd:
     return open_website(website)

 return ask_gpt(cmd)

 


def wait_for_wake_word():
  while True:
    command = input("You: ")
    if "jarvis" in command.lower():
      speak("I am here.")
      break

def main():
 
 while True:
  wait_for_wake_word()
 
  speak("Initializing Jarvis");
  
  while True:
   command = take_command()

  #  if not command:
  #   speak("Sorry, I didn't catch that. Please repeat.")
  #   continue

   if "sleep" in command.lower():
     speak("Bye.")
     break

   response = process_command(command)
   speak(response)


main()


