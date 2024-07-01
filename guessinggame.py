'''
    Developed by: James Ald Teves
    BS Computer Science
    CCS 1 - C

    Description: This program is a simple guessing games with a simple input and output
'''

import random

def main():
    print ("I am James Ald Y. Teves, a Computer Science freshman")
    print ("I am welcoming you to my guessing game, hoping that you would enjoy up til the end.")
    number = random.randint (1, 100)
    guess = float (input("Guess a number between 1 and 100: "))
    guesses = 0
    LastGuesses = None
    
    
    while guess == guess:
        if LastGuesses == guess:
                print("You cannot input the same guess consecutively")
                print("Current guess counter is: {} \n".format(guesses))
                guess = float(input("Guess a number between 1 and 100: "))
        else:
            if guess > 100 or guess < 1:
                print ("Invalid. 1 to 100 only are applicable.")
                guess = float (input("\nGuess a number between 1 and 100: "))
            else:
                if guess < number:
                    LastGuesses = guesses
                    guesses += 1
                    print ("You need to guess higher. Try again.")
                    guess = float (input("\nGuess a number between 1 and 100: "))
                elif guess > number:
                    LastGuesses = guesses
                    guesses += 1
                    print ("You need to guess lower. Try again.")
                    guess = float (input("\nGuess a number between 1  100: "))
                elif guess == number:
                    print("You have guessed the number correctly!")
                    print("Congratulations, it took you {} guesses!".format(guesses))
                    while True:
                        restart = input('Do you want to try again?')
                        if restart.lower().startswith("y"):
                            main()
                        elif restart.lower().startswith("n"):
                            print("Hope you enjoy, thank for playing!")
                            exit()
                            break
                    
main()
            
