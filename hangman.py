# Hangman
MAX_NUMBER_OF_GUESSES = 3
MASK = "_"

play_new_game = True
while play_new_game:
    word_to_guess = input("Enter a word: ")
    masked_word = [MASK] * len(word_to_guess)
    correct_guessed_letters = 0

    current_guess_count = 0
    while current_guess_count < MAX_NUMBER_OF_GUESSES and correct_guessed_letters < len(word_to_guess):
        print("Current state:", masked_word)
        guess = input("Make your next guess: ")

        good_guess = False  # Flag to see if this guess should be "counted" or not.

        if len(guess) == 1:
            i = 0
            while i < len(word_to_guess):
                if guess == word_to_guess[i] and masked_word[i] == MASK:
                    masked_word[i] = word_to_guess[i]
                    correct_guessed_letters = correct_guessed_letters + 1
                    good_guess = True
                i = i + 1
        elif guess == word_to_guess:
            correct_guessed_letters = len(word_to_guess)
            good_guess = True

        if not good_guess:
            current_guess_count = current_guess_count + 1

    if correct_guessed_letters == len(word_to_guess):
        print("You won")
    else:
        print("You lost")

    continue_ = input("Do you want to go again? (Yes or No)")
    play_new_game = continue_ == "Yes" or continue_ == "YES" or continue_ == "yes"
