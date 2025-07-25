#number guessing game
import random

c_guess = random.randint(1,100) #computer picks a random number

#to assign attempts
used_attempts = 0
max_attempts = 7
#using for loop for fixed number of trials
while used_attempts < max_attempts:
    #to validate the number
    try:
        your_guess = int(input('Enter your guess(1-100): '))
    except ValueError:
        print('Please enter a number')
        continue

    #to check if the number is in the range
    if not your_guess in range(1,100):
        print('Please enter a number between 1 and 100')
        continue

    #only get to the next attempt if the input is a valid one
    used_attempts += 1

    #for assigning the score
    if your_guess == c_guess:
        print(f'Correct 🥳! You guessed in {used_attempts} trials')
        break
    elif your_guess > c_guess:
        print('Your guess is too high🌕')
    elif your_guess < c_guess:
        print('Your guess is too low🌑')

#printing a messege if user can't guess after trials r over
else:
    print(f'Game over😞, your number was {c_guess}')