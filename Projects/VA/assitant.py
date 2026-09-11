"""
gTTS-->Google text to speech
"""
from gtts import gTTS
text=gTTS("Hello guys,how are you doing?")
text.save("audio.mp3")
