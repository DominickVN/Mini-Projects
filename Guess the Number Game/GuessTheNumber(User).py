import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        if guess < random_number:
            print('Sorry, guess again. Your number was too low. ')
            guesses += 1
        elif guess > random_number:
            print('Sorry, guess again. Your number was too high' )
            guesses += 1
        else : guesses +=1

    print(f'Congrats! You guessed the random number, {random_number}, correctly! It took you ' + str(guesses) + ' guesses to find the random number! ')

guess(10)