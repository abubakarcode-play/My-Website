import random
import time

def intro(number):
    """Ask for player's name and tell them whether the number is odd/even."""
    global name
    name = input("May I ask you for your name? ").strip()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 100.")
    x = 'even' if number % 2 == 0 else 'odd'
    print(f"\nThis is an {x} number.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick(number):
    """Main guessing loop: player has up to 6 valid guesses."""
    guessesTaken = 0
    max_guesses = 6

    while guessesTaken < max_guesses:
        time.sleep(0.25)
        enter = input("Guess: ").strip()

        try:
            guess = int(enter)  # convert guess to integer

            if 1 <= guess <= 100:
                guessesTaken += 1

                if guess < number:
                    print("The number that you have entered is too low.")
                elif guess > number:
                    print("The number that you have entered is too high.")
                else:  # guess == number
                    print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
                    return
            else:
                print("Silly Goose! That number isn't in the range 1-100!")
        except ValueError:
            print(f"I don't think that '{enter}' is a number. Sorry.")

    # if loop ends without guessing correctly
    print(f"Sorry, {name}. You didn't guess my number. The number was {number}.")

def game():
    """Full game loop with replay option."""
    while True:
        number = random.randint(1, 100)
        intro(number)
        pick(number)

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print(f"Thanks for playing, {name}! Goodbye 👋")
            break

if __name__ == "__main__":
    game()