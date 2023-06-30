def add_songs(*args):
    songs_dict = {}
    for song in args:
        song_name = song[0]
        song_lyrics = song[1]
        if song_name not in songs_dict:
            songs_dict[song_name] = []
        if len(song_lyrics) > 0:
            songs_dict[song_name] += song_lyrics

    result = ""

    for key, value in songs_dict.items():
        result += f"- {key}\n"
        for current_value in value:
            result += current_value + "\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
