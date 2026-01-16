import random

level_dict = {
    'easy': 10,
    'hard': 5
}

def check_attempt(hidden_number, user_guess):
    win = False
    guess = ""

    if user_guess == hidden_number:
        win = True
        return {"win": win}

    guess = "low" if user_guess < hidden_number else "high"

    return {"win": win, "guess": guess}


def main():
    magic_number = random.randint(1, 100)
    print(magic_number)
    attempts = 0
    win = False

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")


    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard':\n--> ")

        if level not in ["easy", "hard"]:
            print("Wrong level choice.\n")
            continue
        
        break

    attempts = level_dict[level]

    while attempts != 0:

        print(f"You have {attempts} attempts remaining to guess the number")

        user_attempt = int(input("Make a guess:\n--> "))

        decision = check_attempt(magic_number, user_attempt)

        if decision["win"]:
            break

        print(f"Too {decision["guess"]}.\n")

        attempts -= 1

    if attempts == 0:
        print(f"It was so simple and yet you could not find it, hidden number was: {magic_number}")
    else:
        print("Hoorah! You guessed it right.")


if __name__ == "__main__":
    main()