import random

def play_game(min_val=1, max_val=100, max_attempts=10):
    secret = random.randint(min_val, max_val)
    attempts = 0

    print(f"🎮 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess → "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("📉 Too low!")
        elif guess > secret:
            print("📈 Too high!")
        else:
            print(f"✅ Congratulations! You guessed it in {attempts} attempts 🎉")
            break
    else:
        print(f"😢 Out of attempts! The secret number was {secret}.")


if __name__ == "__main__":
    play_game()
