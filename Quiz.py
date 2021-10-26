#Start
#Write function that checks the answers
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('sorry wrong answer, please try again')
                attempt = attempt + 1
    if attempt == 3:
        print('The right answer is ' + answer)

#Create a score variable
score = 0 

#Show quiz text to user (esittele peli)
print('Guess the Capital!')

#Tee kysymys ja lue vastaus
guess1 = input('What is the capital of Sweden?')
#check answer / correct answer
check_guess(guess1, 'Stockholm')

guess2 = input('What is the capital of Norway?')
#check answer / correct answer
check_guess(guess2, 'Oslo')

guess3 = input('What is the capital of Russia?')
#check answer / correct answer
check_guess(guess3, 'Moscow')

guess4 = input('The capital of Finland?')
#check answer / correct answer
check_guess(guess4, 'Helsinki')

#Show user score
print('Pistemääräsi on' + str(score))

#End