import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the secret word with guesses."""
    stage_index = max(0, min(mistakes, len(STAGES) - 1))
    print("\n" + "=" * 32)
    print(STAGES[stage_index])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("Guessed:", " ".join(sorted(guessed_letters)) or "(none)")
    print("Mistakes:", mistakes, "/", len(STAGES) - 1)
    print("=" * 32 + "\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    # print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Game loop: continue until win or out of attempts
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win condition: all letters guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman! The word was:", secret_word)
            break

        # Check lose condition: too many mistakes
        if mistakes >= max_mistakes:
            print("Oh no! The snowman melted. The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        # Guard: only letters and single character
        if not guess or not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed '" + guess + "'. Try another letter.")
            continue

        # Record guess
        guessed_letters.append(guess)

        # Update mistakes only if guess not in secret_word
        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess! Mistakes:", mistakes, "/", max_mistakes)
        else:
            print("Nice! '" + guess + "' is in the word.")


def play_again():
    """Ask the user if they want to play another round."""
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def start_game_loop():
    """Run repeated games until the user quits."""
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing Snowman Meltdown! Goodbye.")
            break
