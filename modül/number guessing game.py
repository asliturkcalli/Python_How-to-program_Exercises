import time
import random
print("""****************************

welcome to the number guessing game

guess a random number between 1 and 100
****************************""")
guesswork = 7
random_number = random.randint(1,100)

while True:
    guess =int(input("what is your guess?:"))

    if (guess == random_number):
        print("your number is being questioned....")
        time.sleep(1)
        print("congratulations!")
        print("number is",random_number)
        break
    elif(guess < random_number):
        print("your number is being questioned....")
        time.sleep(1)
        guesswork -= 1
        print("Please say a higher number.")
        print("guesswork:",guesswork)
    else:
        print("your number is being questioned....")
        time.sleep(1)
        guesswork -= 1
        print("Please say a lower number.")
        print("guesswork:",guesswork)
    if (guesswork == 0 ):
        print("Your Guessing Right Done. We are sad")
        print("number:",random_number)
        break
