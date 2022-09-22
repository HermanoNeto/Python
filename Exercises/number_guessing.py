from random import randint
from time import sleep
from replit import clear


logo = """
   _____                       _______ _            _   _                 _
  / ____|                     |__   __| |          | \ | |               | |
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|


"""



def play(chances):
    while not chances == 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            chances -= 1
            if chances == 0:
                print("You've run out of guesses, you lose.")
                break
            print("Guess again.")
            continue
        elif guess < number:
            print("Too Low.")
            chances -= 1
            if chances == 0:
                print("You've run out of guesses, you lose.")
                break
            print("Guess again.")
            continue
        else:
            print(f"You got it! The answer was {number}")
            break


while True:
    number = randint(1, 100)
    print(logo)
    print('')
    print("I'm Thinking of a number between 1 and 100")
    print(number)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip()


    if difficulty == "easy":
        play(10)
    elif difficulty == "hard":
        play(5)
    else:
        print("unknown command. Try again")
        sleep(1)
        clear()
        continue

    sleep(0.4)

    if input("Do you want to play again? 'y' or 'n': ") == "y":
        clear()
        continue
    else:
        break
