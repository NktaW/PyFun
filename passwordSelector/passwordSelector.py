#import sting and random modules from python library.
import random
import string

#Make a list of different words for building new passwords

#List of adjectives
adjectives = ['sleepy', 'fast', 'huge',
              'focused', 'invisible', 'powerful',
              'flawlesss', 'stoic', 'deep',
              'mindull', 'shapless', 'sharp',
              'kind', 'dark', 'silly', 'crazy']
#List of nouns
nouns = ['balloon', 'artist', 'wizard',
         'goat', 'dragon', 'spider',
         'monkey', 'woman', 'knight',
         'hammer', 'dog', 'frog']


#Starting words, Greet the user.
print('Hi there, and welcome to choose a new strong password!')

#Make a while loop that user can have multiple options to choose.
while True:
    for num in range(3):
#Choose word using choise() function, from the pythons random module.
        adjective = random.choice(adjectives)
        noun = random.choice(nouns) 
#Choose a random number using randrange() function, from random module
        number = random.randrange(0, 100)
#Choose a special character using random.choise() function to make a password stronger
        special_char = random.choice(string.punctuation)
#Assemble all parts and create strong password
        password = adjective + noun + str(number) + special_char
        print('Here is you\'re new password: %s' % password)

    response = input('Want a new password ?  Type y or n:  ')
    if response == 'n':
        break
