


import random
from test import spam
best_score = None
class spam :
        
        def guessing_game():
            """this function asks player's name and help them to guess the random number!
            """
            user_name = input('Hi Buddy, What can I call you buddy? ')
            first_name_upper = user_name.capitalize()
            print("Nice to meet you "+ first_name_upper)
            print('incase you got tired press 0 to exit the game!')
            num = random.randint(1, 10)
            guess = None
            tries = 1
            results =[]
            while guess != num:
                
                guess = input( "guess a number between 1 and 10: ")
                try:
                    guess = int(guess)
                except:
                    guess = int(input('please write only numbers between 1 and 10:'))

                if guess > num:
                    print('try to guess a lower number')
                    tries += 1
                    results.append(guess)
                elif guess < num:
                    print ('try to guess a higher number')
                    tries += 1
                    results.append(guess)
                elif guess == num:
                    global best_score
                    print("Congratulations! You guessed correct!")
                    print("It took you {} tries.".format(tries))
                    if best_score == None or tries < best_score:
                        best_score = tries
                    results.append(guess)
                    print("best score so far: {} tries".format(best_score))
                    print(results)
                    spam.Play_again()       
                elif guess == 0:
                    break   

        def Play_again():
            """this function asks users if they want to play a game or not and save the results in a text file.
            """

            play_again = input("Would you like to play again (y or n)? ")
            if play_again.lower() == "y":  
                spam.guessing_game()   
            elif play_again.lower() == "n":
                with open("scores.txt", "r+") as file:
                    hi = file.read()
                    if not hi:  
                        hi = '0'
                    if best_score > int(hi):
                        print("NEW HIGHSCORE!")
                        file.seek(0)  
                        file.write(str(best_score))
                    else:
                        print("HIGHSCORE =%s" % hi)
                        




if __name__ == "__main__":

    spam.guessing_game()
    spam.Play_again()