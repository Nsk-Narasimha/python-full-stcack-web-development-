from gtts import gTTS
import playsound,time,webbrowser,uuid,os,random
import speech_recognition as sr
#import segno
#from segno import helpers
import pyqrcode,png
def listen():
    """Function for specch Recognition"""
    r=sr.Recognizer()
    #we will take microphone
    with sr.Microphone() as source:
        print("listening....")
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
    if "game" in data:
        listening=True
        respond("you want which one.  rock,paper,scissor or number guessing")
        dat=listen().lower()
        if "rock" in dat:
            listening=True
            respond("okay start rock paper scissor say any one only")
            player1=listen().lower().strip()
            player2=random.choice(["rock","paper","scissors"]).lower()
            if(player1 not in ["rock","paper","scissors"]):
                respond("rock/paper/scissor you want pronous correct and tell these only not to other one okay ")
                va(data)
            else:
                print(player1,player2)
                if(player1=='rock' and player2=="paper" or player1=="paper" and player2=="scissors"
                    or player1=="scissors" and player2=="rock"):
                    respond("yes yes i am the winner")
                elif player1==player2:
                    respond("it's draw Man, i will won in the next game")
                else:
                    respond("shit,you are the winner")
        elif "number" in dat:
            listening=True
            respond("it was my favourate game")
            c=0;n=20
            for i in range(3):
                respond(f"Guess the number between 1 to {n}:")
                guess=int(listen())
                g=random.randint(1,n)
                if(0<guess>n):
                    respond("You want to enter between the range,,it will starts from first")
                print(guess,g)
                if(guess==g):respond("you won the game");c=1;break
                else:respond("Try again");n=n-n//2
            if(c==0):respond("You are waste in game; go and study")
    elif "QR code".lower() in data.lower():
        listening=True
        link=input("enter your link:")
        qr=pyqrcode.create(link)
        qr.png("myqr.png",scale=100)
        respond("your qr is done")
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
    elif "bye" in data:
        listening=False
        respond("bye bujji")
    try: return listening
    except UnboundLocalError as e:print("make sure to speak louder and faster")
respond("hi bro we want to play game and i can also generate qrcode")
listening=True
while listening:
    data=listen()
    listening=va(data)

