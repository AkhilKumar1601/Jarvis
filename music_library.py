import webbrowser

songs = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "counting stars": "https://www.youtube.com/watch?v=hT_nvWreIhg",
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "industry baby": "https://www.youtube.com/watch?v=UTHLKHL_whs",
    "alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
    "on my way": "https://www.youtube.com/watch?v=dhYOPzcsbGM",
    "unstoppable": "https://www.youtube.com/watch?v=h3h035Eyz5A"
}

def play_song(song):
  webbrowser.open(songs[song])
  return f"Playing {song}"