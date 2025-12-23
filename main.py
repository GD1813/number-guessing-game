import random


def choose_level():
    level = input("Choose level (easy / medium / hard): ").lower()

    if level == "easy":
        return random.randint(1, 50), 8
    elif level == "medium":
        return random.randint(1, 100), 6
    elif level == "hard":
        return random.randint(1, 100), 4
    else:
        print("Invalid level selected.")
        return None, None


def play_game():
    number, max_attempts = choose_level()

    if number is None:
        return

    print(f"\nYou have {max_attempts} attempts to guess the number!")

    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

    print(f"❌ Game over! The correct number was {number}")


if __name__ == "__main__":
    play_game()
