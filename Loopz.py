#Muuttuja wizards, joka sisältää welhojen määrän.
wizards = 0

#Muuttuja answer sisältää vastauksen welhojen lisäämis kysymykseen.
answer = 'y'

while answer == 'y':
    #lisätään welho
    wizards = wizards + 1
    #Lause näyttää viestin jossa näkyy lisättyjen Welhojen kokonaismäärä
    print('Welhojen määrä on ' + str(wizards))
    #Vastaus tallettuu answer muuttujaan uudeksi arvoksi.
    answer = input('Lisätäänkö Welho ? (y/n)')
