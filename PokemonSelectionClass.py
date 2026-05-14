'''
Created on May 12, 2026

@author: julianbarroso
'''
class pokemonSelection():
    def __init__(self, pokemon):
        self._pokemon = pokemon    
    #getters
    def getPokemon(self):
        return self._pokemon
    #setters   
    def setPokemon(self, newPokemonList):
        self._pokemon = newPokemonList 
    #helperFunctions
    def addPokemon(self, newPokemon):
        self._pokemon.append(newPokemon)
        
    def chooseFirstPokemon(self, trainer, pokemon1):                                                                                                       
        trainer.setCurrentPokemon(pokemon1)     
        trainer.setFirstPokemon(pokemon1) 
              
    def chooseOtherPokemon(self, trainer, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6):
        trainer.setSecondPokemon(pokemon2) 
        trainer.setThirdPokemon(pokemon3) 
        trainer.setFourthPokemon(pokemon4) 
        trainer.setFifthPokemon(pokemon5) 
        trainer.setSixthPokemon(pokemon6) 
        