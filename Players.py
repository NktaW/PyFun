#This program finds the oldest player in the class player object.

class Player:
    Game = 'World of Wizards'
    def __init__(self, name, age):
        self.name = name
        self.age = age


#instantiate the Player object with 3 players
Marco = Player('Marco', 18)
Jane = Player('Jane', 23)
Bruce = Player('Bruce', 28)

#Create function that finds the oldest cat
def get_oldest_player(*args):
    return max(args)

#Output
print(f'The oldest player is {get_oldest_player(Marco.age, Jane.age, Bruce.age)} years old')

