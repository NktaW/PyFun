#Create a Class
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
        #self keyword tekee meidän luomista atribuuteista dynaamisia.
        #name, age ovat atribuutteja
            self.name = name
            self.age = age

    #Funktio Spell
    def Spell(self):
        print('Starting to  cast spell')
        return 'Casting...'

    #Funktio shout
    def shout(self):
        print(f'Hello, my name is {self.name}, i am Wizard, and im {self.age} years old')

#Luo olio...sisältää nimen ja iän
player1 = PlayerCharacter('Bruce', 28)
player2 = PlayerCharacter('Marianne', 22)
player2.run = 'Running'

print(player1.membership)
print(player1.shout())
print(player1.Spell())

print(player2.membership)
print(player2.shout())
print(player2.age)
print(player2.run)