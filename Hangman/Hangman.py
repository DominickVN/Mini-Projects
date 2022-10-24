import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
    guesses = 0

    while len(word_letters) > 0 and lives > 0:
        if guesses < 1:
            print("Welcome to Hangman! \n \n"
                  "Guess a letter to find the word. Keep guessing until you've figured it out! \n \n"
                  f"But be careful!! You only have {lives} lives, and every time you guesss a letter that's not in "
                    "the word, you lose a life. \nRun out of lives and you die!\n")
            guesses += 1

        elif guesses >= 1:
            print(f"You have{lives} lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Unknown letters: ", " ".join(word_list,), "\n")


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")

            else:
                lives = lives - 1
                print("That letter isn't in the word! \n")
        elif user_letter in used_letters:
            print("You already tried that letter. \n Guess again! ")
        else:
            print("That character doesn't work... Try a Letter!")

    if lives == 0:
        print(f'Y O U   D I E D \nThe word was {word}')
    else:
        print(f'You got it! the word was {word}!')


if __name__ == '__main__':
    hangman()