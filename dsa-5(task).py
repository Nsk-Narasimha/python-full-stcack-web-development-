# task 1
import random
def RPS():
    """rock,paper,scissor game / it will return the 0-tie,1-you won,2-computer won"""
    p1,p2=0,0
    player1=input("enter one of these-->rock,paper scissors:").lower().strip()
    player2=random.choice(["rock","paper","scissors"]).lower()
    if(player1 not in ["rock","paper","scissors"]):
        print("enter valid one as rock/paper/scissor")
        return RPS()
    print(player1,player2)
    if(player1=='rock' and player2=="paper" or player1=="paper" and player2=="scissors"
       or player1=="scissors" and player2=="rock"):
        return 2
    elif player1==player2:
        return 0
    else:
        return 1

p1,p2=0,0
for _ in range(10):
    player=RPS()
    if(player==1):
        print("Player1 is won")
        p1+=1
    elif player==0:
        print("Tie")
    else:
        print("Player2 is won")
        p2+=1
print("-----------------------")
print(f"Score:you:{p1} and computer:{p2}")
if(p1>p2):print("You are the winner")
elif(p2>p1):print("AI is  dominated you,,computer is the winner")
else:print("Both are equal-Tie")

# task 2

def numberguess():
    """guess a number from randomized"""
    c=0;n=20
    for i in range(3):
        guess=int(input(f"Guess the number between 1 to {n}:"))
        g=random.randint(1,n)
        if(0<guess>n):
            print("You want to enter between the range,,it will starts from first")
            return numberguess()
        print(guess,g)
        if(guess==g):print("you won the game");c=1;break
        else:print("Try again");n=n-n//2
    if(c==0):print("You are waste in game; go and study")
game=0
while(game!='3'):
    game=input("""enter the your choose:
               1.Rock,Paper,Scissors Game
               2.Guessing Number Game
               3.You want to Study
               Enter 1/2/3:""")
    if(game=='1'):
        player=RPS()
        if(player==1):
            print("You are the winner")
        elif player==0:
            print("Tie")
        else:
            print("Computer is the winner")
    elif(game=='2'):
        numberguess()
    elif(game=='3'):
        print("You want to Study, go and concentrate in it")
    else:
        print("you want to enter based on the choose 1,2,3")


"""
#class as game with rps,number guess
class Game:
    def RPS(self):
        p1,p2=0,0
        player1=input("enter one of these-->rock,paper scissors:").lower().strip()
        player2=random.choice(["rock","paper","scissors"]).lower()
        if(player1 not in ["rock","paper","scissors"]):
            print("enter valid one as rock/paper/scissor")
            return RPS()
        print(player1,player2)
        if(player1=='rock' and player2=="paper" or player1=="paper" and player2=="scissors"
           or player1=="scissors" and player2=="rock"):
            return 2
        elif player1==player2:
            return 0
        else:
            return 1
    def numberguess(self):
        c=0;n=20
        for i in range(3):
            guess=int(input(f"Guess the number between 1 to {n}:"))
            g=random.randint(1,n)
            if(0<guess>n+1):
                print("You want to enter between the range")
                return numberguess()
            print(guess,g)
            if(guess==g):print("you won the game");c=1;break
            else:print("Try again");n=n-n//2
            if(c==0):print("You are waste in game; go and study")
g=Game()
print(g.RPS())
g.numberguess()
            
"""

















