import random,time
'''a=random.randint(1000,9999)
#print(a)
for i in range(4):
    time.sleep(2)
    print(random.randint(1000,9999))
    time.sleep(5)'''
'''player1=input("enter one of these-->rock,paper scissors:").lower().strip()
player2=random.choice(["rock","paper","scissors"]).lower()
print(player1,player2)
if(player1=='rock' and player2=="paper" or player1=="paper" and player2=="scissors"
   or player1=="scissors" and player2=="rock"):
    print("player2 is won")
elif player1==player2:
    print("tie")
else:
    print("player1 is won")
c=0;n=10
for i in range(3):
    guess=int(input(f"guess the number between 1 to {n}:"))
    g=random.randint(1,n)
    print(guess,g)
    if(guess==g):print("you won the game");c=1;break
    else:print("try again");n=n-n//2
if(c==0):print("you are waste in game; go and study")
import random,segno


when = ["A long back", "Once upon a time", "Few years ago"]
who = ["Devara", "King in France", "Barbie Queen"]
what = ["A magical sword", "Powerful Hammer", "Unlimited Arrows"]
where = ["Far in the Galaxy", "End of Ocean", "In India"]
how = ["War started", "Both fought for 15 days", "Sad Ending"]

print(random.choice(when))
print(random.choice(who))
print(random.choice(what))
print(random.choice(where))
print(random.choice(how))'''
import segno
print(dir(segno))
from segno import helpers
qr=helpers.make_mecard(name="Kosuri Narasimha Sai Kumar",email="knsknsk10@gmail.com",phone="+91 7997847720"
                       ,url="https://www.linkedin.com/in/narasimha-sai-kumar-kosuri-a48695289/")
print(qr)
qr.save("mycard.png",scale=10)











    
