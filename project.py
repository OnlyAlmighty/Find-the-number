import random
def project():
    print("Find The number!")
    num = input("Enter your number: ")
    if num == random.randint(0,100):
     print("Correct answer you win")
    else:
        print("You loss re try again!")
repeat = input("Would you like to replay?  ").lower()
if repeat =="yes":
    project()
else:
    print("bye")
    exit()
project()

        
    
