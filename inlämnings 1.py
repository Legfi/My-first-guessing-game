


from math import e
import random


if __name__ == "__main__":
print("hello")
    num = random.randint(1, 10)
    guess = None
    #Exit_program = "exit"
    user_name = input('Hi, What can i call you buddy? ')

    while guess != num:
    
        guess = input("Hi "+ user_name + "! guess a number between 1 and 10: ")
        guess = int(guess)

        if guess < num: 
            print("you need to guess a higher number")
            break
        elif guess > num:
            print("you need to guess a lower number")
        elif guess == num:
            print("congratulations! you won!")
            break
        elif guess == "exit":
            break