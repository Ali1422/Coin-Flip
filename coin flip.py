import random
import time
choices =["heads", "tails"]
print("********************************")
print("welcome to the python coin flip!")
print("********************************")
while True:
    time.sleep (2)
    coin =input("please enter a choice of heads or tails: ")
    if coin == "heads":
        print(" you have chosen",coin)
    elif coin == "tails":
        print("you have chosen",coin)
    else:
        print("invalid choice please try again!")
        exit()
    time.sleep(2)
    print(" we will now begin the toss")
    time.sleep(2)
    print("tossing.......")
    flip = random.choice(choices)
    if coin == flip:
        print("congratulations, you have won! Feel free to play again")
    else:
        print("you have lost! Feel free to try again!")
    time.sleep(3)

