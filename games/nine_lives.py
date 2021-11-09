#import module
import random
#create lives variable
lives = 9
#make list of words
words = ['pizza', 'pasta', 'spoon', 'space', 'green', 'beard', 'phone', 'trade']
#create variable that choose random word from the list
secret_word = random.choice(words)
#create clue variable
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1
#create heart sybol to show user how many lives left
heart_symbol = u'\u2764'
#create variable, wich contains info if user guessed word correctly
guessed_word_correctly = False

unknown_letters = len(secret_word)

#create while loop that checks if letter exist in the guessing word.
def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters

difficulty = input('Choose difficulty level  (level 1, 2, or 3):\n 1 Eazy\n 2 Medium\n 3 Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 9
elif difficulty == 2:
    lives = 6
else:
    lives = 4

while lives > 0:
    print(clue)
    print('Lives remaining' + heart_symbol * lives)
    guess = input('Guess word, or letter of the word:  ')

    #if guessed word is correct the loop breaks
    if guess == secret_word:
        guessed_word_correctly = True
        break
    #if letter exist in guessed word, clue updates
    if guess in secret_word:
        update_clue(guess, secret_word, clue, unknown_letters)
    #if answer incorrect, will lost 1 live
    else:
        print('Incorrect! you lost one live')
        lives = lives - 1
    if unknown_letters == 0:
        guessed_word_correctly = True
        break

if guessed_word_correctly:
    print('Congraz, you won!  Secret word was:  ' + secret_word)
else :
    print('You lost! The secret word was:  ' + secret_word)
