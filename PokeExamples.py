#Mr. McCauley, Julian, Josue, Miguel
from Water import Water
from Electric import Electric
from Fire import Fire
from Steel import Steel
from Rock import Rock
from Trainer import Trainer
from Ice import Ice
import time

def findIndex(inputList, value):
    length = len(inputList)
    for i in range(length):
        if inputList[i] == value:
            return i

#Steel types
lucario = Steel("Lucario")
steelix = Steel("Steelix")
honedge = Steel("Honedge")
doublade = Steel("Doublade")
aegislash = Steel("Aegislash")
aron = Steel("Aron")
lairon = Steel("Lairon")
aggron = Steel("Aggron")
meltan = Steel("Meltan")
melmetal = Steel("Melmetal")
registeel = Steel("Registeel")

steeltypes = [lucario,steelix,honedge, doublade,aegislash,aron,lairon, aggron, meltan, melmetal, registeel]

#Rock types
geodude = Rock("Geodude")
graveler = Rock("Graveler")
golem = Rock("Golem")
onix = Rock("Onix")
kabuto = Rock("Kabuto")
kabutops = Rock("Kabutops")
tyrunt = Rock("Tyrunt")
tyrantrum = Rock("Tyrantrum")
sudowoodo = Rock("Sudowoodo")
aerodactyl = Rock("Aerodactyl")
regirock = Rock("Regirock")

rocktypes = [geodude, graveler, golem, onix, kabuto, kabutops, tyrunt, tyrantrum, sudowoodo, aerodactyl, regirock]
#Water types
squirtle = Water("Squirtle")
wartortle = Water("Wartortle")
blastoise = Water("Blastoise")
poliwag = Water("Poliwag")
poliwhirl = Water("Poliwhirl")
poliwrath = Water("Poliwrath")
magikarp = Water("Magikarp")
gyarados = Water("Gyarados")
tentacool = Water("Tentacool")
tentacruel = Water("Tentacruel")
kyogre = Water("Kyogre")

watertypes = [squirtle, wartortle, blastoise, poliwag, poliwhirl, poliwrath, magikarp, gyarados, tentacool, tentacruel, kyogre]
#Fire types
arcanine = Fire("Arcanine")
growlithe = Fire("Growlithe")
vulpix = Fire("Vulpix")
nintetales = Fire("Ninetales")
charmander = Fire("Charmander")
charmeleon = Fire("Charmeleon")
charizard = Fire("Charizard")
fuecoco = Fire("Fuecoco")
crocalor = Fire("Crocalor")
skeledirge = Fire("Skeledirge")
moltres = Fire("Moltres")

firetypes = [arcanine, growlithe, vulpix, nintetales, charmander, charmeleon, charizard, fuecoco, crocalor, skeledirge, moltres]
#Electric types
voltorb = Electric("Voltorb")
electrode = Electric("Electrode")
shinx = Electric("Shinx")
luxio = Electric("Luxio")
luxray = Electric("Luxray")
electrike = Electric("Electrike")
manectric = Electric("Manectric")
rotom = Electric("Rotom")
electabuzz = Electric("Electabuzz")
ampharos = Electric("Ampharos")
zapdos = Electric("Zapdos")

electrictypes = [voltorb, electrode, shinx, luxio, luxray, electrike, manectric, rotom, electabuzz, ampharos, zapdos]
#Ice types
cloyster = Ice("Cloyster")
swinub = Ice("Swinub")
piloswine = Ice("Piloswine")
spheal = Ice("Spheal")
sealeo = Ice("Sealeo")
walrein = Ice("Walrein")
snover = Ice("Snover")
abomasnow = Ice("Abomasnow")
beartic = Ice("Beartic")
mamoswine = Ice("Mamoswine")
articuno = Ice("Articuno")

icetypes = [cloyster, swinub, piloswine, spheal, sealeo, walrein, snover, abomasnow, beartic, mamoswine, articuno]
icepokemanNames = []
allpokemonNames = []

allpokemon = [cloyster, swinub, piloswine, spheal, sealeo, walrein, snover, abomasnow, beartic, mamoswine, articuno, voltorb, electrode, shinx, luxio, luxray, electrike, manectric, rotom, electabuzz, ampharos, zapdos, arcanine, growlithe, vulpix, nintetales, charmander, charmeleon, charizard, fuecoco, crocalor, skeledirge, moltres, squirtle, wartortle, blastoise, poliwag, poliwhirl, poliwrath, magikarp, gyarados, tentacool, tentacruel, kyogre, geodude, graveler, golem, onix, kabuto, kabutops, tyrunt, tyrantrum, sudowoodo, aerodactyl, regirock, lucario,steelix,honedge, doublade,aegislash,aron,lairon, aggron, meltan, melmetal, registeel]

for pokemon in icetypes:
    icepokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())
electricpokemanNames = []
for pokemon in electrictypes:
    electricpokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())
firepokemanNames = []
for pokemon in firetypes:
    firepokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())
waterpokemanNames = []
for pokemon in watertypes:
    waterpokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())
rockpokemanNames = []
for pokemon in rocktypes:
    rockpokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())
steelpokemanNames = []
for pokemon in steeltypes:
    steelpokemanNames.append(pokemon.getName())
    allpokemonNames.append(pokemon.getName())





player1Alive = True
player2Alive = True
player1Name = input("Enter the name of the first trainer:")
player2Name = input("Enter the name of the second trainer:")

player1Pokemon = []
player2Pokemon = []
player1PokemonNames = []
player2PokemonNames = []
#Make lists for the names of types =(
def choosePokemon(length, playerList, playerList2, Player, numberOfPokemon):
    trueness = False
    count = 0
    while trueness == False:  
        print("Steel types:")
        print(steelpokemanNames)
        print("Rock types:")
        print(rockpokemanNames)
        print("Water types:")
        print(waterpokemanNames)
        print("Fire types:")
        print(firepokemanNames)
        print("Electric types:")
        print(electricpokemanNames)
        print("Ice types:")
        print(icepokemanNames)
        print(allpokemonNames)
        selectedPokemon = input(f"Pick your pokemon,{Player}!, you have {numberOfPokemon} pokemon right now!")
        for i in range (length):
            if selectedPokemon.lower() == allpokemonNames[i].lower():
                print(f"You got a {allpokemonNames[i]}!")
                time.sleep(5)
                playerList2.append(allpokemon[i].getName())
                playerList.append(allpokemon[i])
                actualPokemon = allpokemonNames[i]
                if allpokemon[i].getType() == "Ice":
                    indexValue = findIndex(icepokemanNames, allpokemonNames[i])
                    icepokemanNames.remove(allpokemonNames[i]) 
                    icetypes.remove(icetypes[indexValue])
                    count = 1
                    break
                elif allpokemon[i].getType() == "Electric":
                    indexValue = findIndex(electricpokemanNames, allpokemonNames[i])
                    electricpokemanNames.remove(allpokemonNames[i])
                    electrictypes.remove(electrictypes[indexValue])
                    count = 1
                    break
                elif allpokemon[i].getType() == "Fire":
                    indexValue = findIndex(firepokemanNames, allpokemonNames[i])
                    firepokemanNames.remove(allpokemonNames[i])
                    firetypes.remove(firetypes[indexValue])
                    count = 1
                    break
                elif allpokemon[i].getType() == "Water":
                    indexValue = findIndex(waterpokemanNames, allpokemonNames[i])
                    waterpokemanNames.remove(allpokemonNames[i])
                    watertypes.remove(watertypes[indexValue])
                    count = 1
                    break
                elif allpokemon[i].getType() == "Rock":
                    indexValue = findIndex(rockpokemanNames, allpokemonNames[i])
                    rockpokemanNames.remove(allpokemonNames[i])
                    rocktypes.remove(rocktypes[indexValue])
                    count = 1
                    break
                elif allpokemon[i].getType() == "Steel":
                    indexValue = findIndex(steelpokemanNames, allpokemonNames[i])
                    steelpokemanNames.remove(allpokemonNames[i]) 
                    steeltypes.remove(steeltypes[indexValue])
                    count = 1
                    break  
        if count == 0:
            print("Please chose a valid pokemon!")
            time.sleep(2)
            continue
        else:
            indexValue = findIndex(allpokemonNames, actualPokemon)
            allpokemonNames.remove(actualPokemon)
            allpokemon.remove(allpokemon[indexValue])
            break

choosePokemon(len(allpokemonNames), player1Pokemon, player1PokemonNames, player1Name, 0)
choosePokemon(len(allpokemonNames), player1Pokemon, player1PokemonNames, player1Name, 1)
choosePokemon(len(allpokemonNames), player1Pokemon, player1PokemonNames, player1Name, 2)
choosePokemon(len(allpokemonNames), player1Pokemon, player1PokemonNames, player1Name, 3)
print(f"You have all your pokemon {player1Name}!")
time.sleep(3)

print(f"Now its your turn {player2Name}!")
choosePokemon(len(allpokemonNames), player2Pokemon, player2PokemonNames, player2Name, 0)
choosePokemon(len(allpokemonNames), player2Pokemon, player2PokemonNames, player2Name, 1)
choosePokemon(len(allpokemonNames), player2Pokemon, player2PokemonNames, player2Name, 2)
choosePokemon(len(allpokemonNames), player2Pokemon, player2PokemonNames, player2Name, 3)
print(f"You have all your pokemon {player2Name}!")
time.sleep(3)

trainer1 = Trainer(player1Name, player1Pokemon[0], player1Pokemon[1], player1Pokemon[2], player1Pokemon[3])
trainer2 = Trainer(player2Name, player2Pokemon[0], player2Pokemon[1], player2Pokemon[2], player2Pokemon[3])

inaccurate = False
while inaccurate == False:
    try:     
        print(f"{player1Name}, what Pokemon will you use first?")
        print(f"Type in 1 for {player1PokemonNames[0]}")
        print(f"Type in 2 for {player1PokemonNames[1]}")
        print(f"Type in 3 for {player1PokemonNames[2]}")
        print(f"Type in 4 for {player1PokemonNames[3]}")
        currentPokenumber = input(f"{player1Name}, what will you chose?")
        if int(currentPokenumber) == 1:
            trainer1._currentPoke = player1Pokemon[0]
            trainer1._firstPoke = player1Pokemon[0]
            trainer1._secondPoke = player1Pokemon[1]
            trainer1._thirdPoke = player1Pokemon[2]
            trainer1._fourthPoke = player1Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 2:
            trainer1._currentPoke = player1Pokemon[1]
            trainer1._firstPoke = player1Pokemon[1]
            trainer1._secondPoke = player1Pokemon[0]
            trainer1._thirdPoke = player1Pokemon[2]
            trainer1._fourthPoke = player1Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 3:
            trainer1._currentPoke = player1Pokemon[2]
            trainer1._firstPoke = player1Pokemon[2]
            trainer1._secondPoke = player1Pokemon[0]
            trainer1._thirdPoke = player1Pokemon[1]
            trainer1._fourthPoke = player1Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 4:
            trainer1._currentPoke = player1Pokemon[3]
            trainer1._firstPoke = player1Pokemon[3]
            trainer1._secondPoke = player1Pokemon[0]
            trainer1._thirdPoke = player1Pokemon[1]
            trainer1._fourthPoke = player1Pokemon[2]
            inaccurate = True
        else:
            print("Please type either 1,2,3 or 4")
        
    except:
        print("Please type either 1,2,3 or 4")          
inaccurate = False
while inaccurate == False:
    try:
        print(f"{player2Name}, what Pokemon will you use first?")
        print(f"Type in 1 for {player2PokemonNames[0]}")
        print(f"Type in 2 for {player2PokemonNames[1]}")
        print(f"Type in 3 for {player2PokemonNames[2]}")
        print(f"Type in 4 for {player2PokemonNames[3]}")
        currentPokenumber = input(f"{player2Name}, what will you chose?")
        if int(currentPokenumber) == 1:
            trainer2._currentPoke = player2Pokemon[0]
            trainer2._firstPoke = player2Pokemon[0]
            trainer2._secondPoke = player2Pokemon[1]
            trainer2._thirdPoke = player2Pokemon[2]
            trainer2._fourthPoke = player2Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 2:
            trainer2._currentPoke = player2Pokemon[1]
            trainer2._firstPoke = player2Pokemon[1]
            trainer2._secondPoke = player2Pokemon[0]
            trainer2._thirdPoke = player2Pokemon[2]
            trainer2._fourthPoke = player2Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 3:
            trainer2._currentPoke = player2Pokemon[2]
            trainer2._firstPoke = player2Pokemon[2]
            trainer2._secondPoke = player2Pokemon[0]
            trainer2._thirdPoke = player2Pokemon[1]
            trainer2._fourthPoke = player2Pokemon[3]
            inaccurate = True
        elif int(currentPokenumber) == 4:
            trainer2._currentPoke = player2Pokemon[3]
            trainer2._firstPoke = player2Pokemon[3]
            trainer2._secondPoke = player2Pokemon[0]
            trainer2._thirdPoke = player2Pokemon[1]
            trainer2._fourthPoke = player2Pokemon[2]
            inaccurate = True
        else:
            print("Please type either 1,2,3 or 4")
    except:
        print("Please type either 1,2,3 or 4")
time.sleep(3)    
print(f"{player1Name} sends out {trainer1._currentPoke.getName()}!")
time.sleep(3)
print(f"{player2Name} sends out {trainer2._currentPoke.getName()}!")
time.sleep(3)
#Both players pick their moves, depending on speeds one pokemon uses a move before the others

while player1Alive and player2Alive:
    accurate = False
    while accurate == False:
        print(f"{trainer1.getName()}, what will {trainer1._currentPoke.getName()} do?")
        print(f"{trainer1._currentPoke.getAttackNames()}")
        try:
            userInput = int(input("Type in 1, 2 or 3 for the corresponding moves:"))
            player1move = trainer1._currentPoke._attackNames[userInput-1]
            player1damage = trainer1._currentPoke._attackDmg[userInput-1]
            if userInput == 1 or userInput == 2 or userInput == 3:
                accurate = True
            else:
                print("Please input 1, 2 or 3 for your move")
                accurate = False
        except:
            print("Please input 1, 2 or 3 for your move")
    accurate = False
    while accurate == False:
        print(f"{trainer2.getName()}, what will {trainer2._currentPoke.getName()} do?")
        print(f"{trainer2._currentPoke.getAttackNames()}")
        try:
            userInput = int(input("Type in 1, 2 or 3 for the corresponding moves:"))
            player2move = trainer2._currentPoke._attackNames[userInput-1]
            player2damage = trainer2._currentPoke._attackDmg[userInput-1]
            if userInput == 1 or userInput == 2 or userInput == 3:
                accurate = True
            else:
                print("Please input 1, 2 or 3 for your move")
                accurate = False
        except:
            print("Please input 1, 2 or 3 for your move")
"""
    speed1 = trainer1._currentPoke.getSpeed()
    speed2 = trainer2._currentPoke.getSpeed()
    if speed1 > speed2:
        print("")
        #Code the battle round so that player 1s move goes before player 2, if player 1s pokemon defeats player 2s pokemon, player 2 should switch to their next pokemon, and speeds should be compared again (continue)
    elif speed2 > speed1:
        print("")
        #Code the battle round so that player 2s move goes before player 2, if player 2s pokemon defeats player 1s pokemon, player 1 should switch to their next pokemon, and speeds should be compared again (continue)
    else:
        #There is a chance that the speeds of both pokemon are the same, so its just random who goes first
        #if speeds are still the same at the end of the player's turns, the chance should be run again
        chance = random.randint(0,1)
        if chance == 0:
            print("")
            #Code the battle round so that player 1s move goes before player 2, if player 1s pokemon defeats player 2s pokemon, player 2 should switch to their next pokemon, and speeds should be compared again (continue)
        elif chance == 1:
            print("")
            #Code the battle round so that player 2s move goes before player 2, if player 2s pokemon defeats player 1s pokemon, player 1 should switch to their next pokemon, and speeds should be compared again (continue)
"""

            
            
    
