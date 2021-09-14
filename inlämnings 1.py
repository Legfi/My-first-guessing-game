


import random

best_score = None

def guessing_game():
    """this function asks player's name and help them to guess the random number!
    """
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
            if 10 > guess > num:
                print('try to guess a lower number')
                tries += 1
                results.append(guess)
            elif 0 < guess < num:
                print ('try to guess a higher number')
                tries += 1
                results.append(guess)
            elif guess == ' ':
                print('please enter only numbers!')    
            elif guess == num:
                global best_score
                print("Congratulations! You guessed correct!")
                print("It took you {} tries.".format(tries))
                if best_score == None or tries < best_score:
                    best_score = tries
                results.append(guess)
                print("best score so far: {} tries".format(best_score))
                print(results)
                Play_again()
            elif guess == 0:
                break
        except ValueError:
            print('please enter only numbers!')
            continue
def Play_again():
    """this function asks users if they want to play a game or not and save the results in a text file.
    """
    play_again = input("Would you like to play again (y or n)? ")
    if play_again.lower() == "y":  
        guessing_game()

def adding_results(best_score : int, first_name_upper : str):
    """this fuction save the best result of the game at a text file.
    Args:
        best_score (int): it's the highest sccore of the game.
    Returns:
        int: updated high score at the text file.
    """
    with open("scores.txt", "a") as file:
        high_score = file.writelines("\n"+ "best score: {} tries".format(best_score)+ " by "+ first_name_upper)
        return high_score


if __name__ == "__main__":

    user_name = input('Hi Buddy, What can I call you? ')
    first_name_upper = user_name.capitalize()
    guessing_game()
    adding_results(best_score, first_name_upper)