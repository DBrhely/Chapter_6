 #Challenge 1
#11/18/14
#Danielle Brhely
#
#Design
#
#make the program to have 1 step
##################################

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

