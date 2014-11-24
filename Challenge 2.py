#Challenge 2
#11/20/14
#Danielle Brhely
#
#Design
#
#def the function that contain a guess hoop
#guess a number
#print the answer
########################

#Function
def ask_number(guess, tried, answer):
    while guess != answer:
       if guess > answer:
           tried +=1
           guess = int(input("Enter a lower number. "))
       elif guess < answer:
            tried += 1
            guess = int(input("Enter a higher number. "))
       else:
            print("Wrong number.")
    tried += 1
    return tried
#Main
import random

tried = 0
answer = random.randint(1,100)
print("Welcome to the guessing game!")
print("Guess the answer in the less amount of tried.")
guess = int(input("\nEnter a number between 1 to 100. "))
#return
tried = ask_number(guess, tried, answer)

#Ending
if tried < 6:
    print("Anwesome, its only took you ",tried,"tries!")
else:
    print("What took you so long, You took ",tried,"tries!")

input("\nPress <Enter> to exit....")
