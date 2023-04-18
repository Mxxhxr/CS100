# Maahir Vohra
# CS100 Section 008
# HW 08, March 23, 2023
import random

randomNum = random.randint(0, 50)
maxAtmpt = 5
numAtmpt = 0

while numAtmpt < maxAtmpt:
    numAtmpt += 1
    userGuess = input("Guess " + str(numAtmpt) + " ? ")
    if int(userGuess) < int(randomNum):
        print(str(userGuess) + " is too low.")

    elif int(userGuess) > int(randomNum):
        print(str(userGuess) + " is too high.")

    else:
        print("You are right! I was thinking of " + str(randomNum))
        break
if numAtmpt == maxAtmpt:
    print("Sorry BITCH you used up all your attempts. The number I was thinking of was " + str(randomNum))
