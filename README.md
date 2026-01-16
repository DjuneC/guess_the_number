# Simple Number Guessing Game

This is a simple number guessing game where you try to guess a hidden number!

## How to Play

1.  **Choose Difficulty:** The game offers two difficulty levels:
    *   **Easy:** You will have 10 attempts to find the hidden number.
    *   **Hard:** You will have 5 attempts to find the hidden number.

2.  **Make a Guess:** Enter your guess at the prompt.

3.  **Receive Feedback:** The game will respond with one of the following messages:
    *   `Too low!` if your guess is less than the hidden number.
    *   `Too high!` if your guess is greater than the hidden number.
    *   `You win!` if your guess is exactly equal to the hidden number.

4.  **Keep Guessing:**  Continue guessing until you correctly identify the hidden number.

## Difficulty Levels

*   **Easy:**  Attempts number:  10
*   **Hard:** Attempts number: 5

## Example Gameplay (Easy Difficulty)

```
Enter difficulty (easy/hard): easy
You have 10 attempts remaining to guess the number.

Guess a number: 5
Too low!

Guess a number: 8
Too high!

Guess a number: 6
Too low!

Guess a number: 7
You win! The hidden number was 7!
```

## Notes

*   This is a basic implementation and does not include error handling for invalid input (e.g., non-numeric input).  You 
could add code to handle this in a more robust version.
*   The game doesn't keep track of the number of guesses you've made.
*   It's just for fun!

---

**[https://github.com/DjuneC/guess_the_number.git]**
