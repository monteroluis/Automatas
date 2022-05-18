import os
from gtts import gTTS


def voice(text, language):
     tts = gTTS(text,language)
     tts.save("./multimedia/audio.mp3")
     os.system("mpg123 " + "./multimedia/audio.mp3")





