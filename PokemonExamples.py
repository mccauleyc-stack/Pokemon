import random
from Water import Water
from Electric import Electric
from Fire import Fire
from Steel import Steel
from Rock import Rock
from Trainer import Trainer
from Ice import Ice
from PokemonBattleClass import Battle

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

pokemon = [steeltypes, rocktypes, watertypes, firetypes, electrictypes, icetypes]

def addRandomPokemon(pokemonList):
    randomType = random.randint(0,5)
    randomPokemon = random.randint(0,10)
    pokemonList.append(pokemon[randomType][randomPokemon])    

player1Alive = True
player2Alive = True
player1Name = input("Enter the name of the first trainer:")
player2Name = input("Enter the name of the second trainer:")

player1Pokemon = []
addRandomPokemon(player1Pokemon)*6

print(f"{player1Name} has a {player1Pokemon[0].getName()}, {player1Pokemon[1].getName()}, {player1Pokemon[2].getName()}, {player1Pokemon[3].getName()}, {player1Pokemon[4].getName()} and a {player1Pokemon[5].getName()}!")

player2Pokemon = []
addRandomPokemon(player2Pokemon)*6

print(f"{player2Name} has a {player2Pokemon[0].getName()}, {player2Pokemon[1].getName()}, {player2Pokemon[2].getName()}, {player2Pokemon[3].getName()}, {player2Pokemon[4].getName()} and a {player2Pokemon[5].getName()}!")


trainer1 = Trainer(player1Name, player1Pokemon)
trainer2 = Trainer(player2Name, player2Pokemon)

battle = Battle(trainer1.getPokemon(), trainer2.getPokemon())

battle.choosePokemon(trainer1, trainer2)

battle.battle(trainer1, trainer2)
