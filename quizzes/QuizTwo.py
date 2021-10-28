#Start

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Congraz! Your answer is correct.')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer, plase try again')
                attempt = attempt + 1
    if attempt == 3:
        print('The right answer is ' + answer)

#Create a score variable 
score = 0

#Start quiz, show questions for user
print('Guess the right answer')

#Create question
guess1 = input('How many hearts does Octopus have ? \n \
A) Three\n B) One\n C) Seven\n \
        What is your answer ? A, B, or C')
check_guess(guess1, 'A')

guess2 = input('6 * 6 = 36? \n \
    Yes or No')
check_guess(guess2, 'Yes')

#Show score to user
print('Your score is ' + str(score))