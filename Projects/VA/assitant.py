"""
libraries
gTTS-->Google text to speech
playsound,pyaudio,time,webbrowser,uuid,speech recognition
"""
'''
from gtts import gTTS
import playsound
text=gTTS("Hello guys,how are you doing?")
text.save("audio.mp3")
playsound.playsound("audio.mp3")'''
from gtts import gTTS
import playsound,time,webbrowser,uuid,os
import speech_recognition as sr
def listen():
    """Function for specch Recognition"""
    r=sr.Recognizer()
    #we will take microphone
    with sr.Microphone() as source:
        respond("strat talking now")
        audio=r.listen(source,phrase_time_limit=10)
    #we need to give our text as voice
    data=""
    #here we will give exceptions(try,except)
    try:
        data=r.recognize_google(audio)
        print("you said:",data)
    except sr.UnknownValueError as e:
        print("request failed")
    except sr.RequestError as e:
        print("speak clearly request is failing")
    return data
    #tts=gTTS(data)
    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")
def respond(string):
    """function to respond back"""
    print(string)
    tts=gTTS(string)
    tts.save("speech.mp3")
    #using uuid---audio file
    filename="speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def va(data):
    if "how are you" in data:
        listening=True
        respond("I am fine thanks for asking")
    elif "what are you doing" in data:
        listening=True
        respond("i am thinking about sanjay he is the attitude star i like him")
    elif "where are you" in data:
        listening=True
        respond("i am in your heart ,you are my heart")
    elif "time" in data:
        listening=True
        respond(time.ctime())
    elif "locate" in data:
        listening = True
        webbrowser.open("https://www.google.com/maps/search/"+ data.replace("locate",""))
        respond("Located")
    elif "open Google" in data:
        listening=True
        webbrowser.open("https://www.google.com")
        respond("opened")
    elif "stop talking" in data:
        listening=True
        respond("bangaram chepana bangaram chepana niku okati chepanaaa bangram  bye")
    elif "smile please" in data:
        listening=False
        respond("heeeeeeee heeeeee heeee hee he he heee heee heeee heeee heee heee  heee heee ")
    try: return listening
    except UnboundLocalError as e:print("make sure to speak louder and faster")
respond("vochesadura vedu vochesadura vedu")
listening=True
while listening:
    data=listen()
    listening=va(data)

