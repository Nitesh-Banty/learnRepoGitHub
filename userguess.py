## use random module devlope a mini game 
#user choice and ganarete random nomber
#and count total guesse
# and write highscore a file
import random
compguess = random.randint(1,100)
print(compguess )
userguess=None
guesses=0
while(compguess!=userguess):
    guesses=guesses+1
    userguess=int(input('Enter your guesses'))
    if(compguess>userguess):
        print('your guesses it wrong! plx enter a larger nomber')
    elif(compguess<userguess):
        print('your guesses it worng! plz ente a lower nober')
    elif(compguess==userguess):
        print(f"your guesses write {guesses} guesses")


        with open('highscore.text') as f:
            highscore=int(f.read())    # this read function read a string so typcasting change the type
            print(f"last high score is{highscore}")
        if(guesses<highscore):
            print('you borken the last score')
            with open("highscore.text","w") as f:
                 f.write(str(guesses))
