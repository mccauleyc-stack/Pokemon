'''
Created on Jan 23, 2026

@author: julianbarroso
'''
import random
import copy

class Battle():
    def __init__(self, p1Pokemons, p2Pokemons):
        self._p1Pokemon = p1Pokemons
        self._p2Pokemon = p2Pokemons
        
    #getters    
    def getP1pokemon(self):
        return self._p1Pokemon #list
    def getP2pokemon(self):
        return self._p2Pokemon #list
    
    #setters 
    def setP1Pokemon(self, newPokemon): #list
        self._p1Pokemon = newPokemon        
    def setP2Pokemon(self, newPokemon): #list
        self._p2Pokemon = newPokemon
    
    #helper functions
    # edit to be able to choose the 4 pokemons
    def choosePokemonOrder(self, trainer, pokemons):# 1 or 2 , player's pokemons (list)
        inaccurate = False                                                                                                                                                      
        while inaccurate == False:                                                                                                                                              
            try:                                                                                                                                                                
                currentPokenumber = int(input(f"{trainer.getName()}, what Pokemon will you use first? \nType in 1 for {pokemons[0].getName()} or 2 for {pokemons[1].getName()} or 3 for {pokemons[2].getName()} or 4 for {pokemons[3].getName()}: "))   
                if int(currentPokenumber) == 1:
                    inaccurate = True  
                elif int(currentPokenumber) == 2:
                    trainer._currentPoke = pokemons[1]                                                                                                                       
                    trainer._firstPoke = pokemons[1]                                                                                                                         
                    trainer._secondPoke = pokemons[0]
                    trainer._thirdPoke = pokemons[2] 
                    trainer._fourthPoke = pokemons[3]
                    inaccurate = True   
                elif int(currentPokenumber) == 3:
                    trainer._currentPoke = pokemons[2] 
                    trainer._firstPoke = pokemons[2]
                    trainer._secondPoke = pokemons[0] 
                    trainer._thirdPoke = pokemons[1]
                    trainer._fourthPoke = pokemons[3]
                    inaccurate = True 
                elif int(currentPokenumber) == 4:   
                    trainer._currentPoke = pokemons[3] 
                    trainer._firstPoke = pokemons[3]
                    trainer._secondPoke = pokemons[0] 
                    trainer._thirdPoke = pokemons[1]
                    trainer._fourthPoke = pokemons[2]
                    inaccurate = True             
            except:
                print("Please type either 1, 2, 3 or 4")                                                                                                                     
        
    def compareSpeeds(self, speed1, speed2): 
        if speed1 > speed2:
            return True
        elif speed1 < speed2:
            return False
        else:
            chance = random.randint(0,1)   
            if chance == 0:
                return True
            elif chance == 1:
                return False       
    
    def chooseMove(self, trainer):                                                                           
            while True:     
                print("")                                                               
                print(f"{trainer.getName()}, what will {trainer._currentPoke.getName()} do?")         
                print(f"{trainer._currentPoke.getAttackNames()}")                                      
                try:                                                                                   
                    userInput = int(input("Type in 1, 2 or 3 for the corresponding moves:"))            
                    pokemonMove = trainer._currentPoke.getAttackNames()[userInput-1]                       
                    moveDmg = trainer._currentPoke.getAttackDmg()[userInput-1]
                    if (userInput == 1) or (userInput == 2) or (userInput == 3):                              
                        return pokemonMove, moveDmg                                                                                                                                                                 
                except IndexError:
                    print("Type in a valid number: 1, 2 or 3")
                except ValueError:
                    print("Type in a valid number: 1, 2 or 3")
                               
    def checkAlive(self, trainer):
        if ( trainer._firstPoke.getCurrentHealth() == 0 ) and ( trainer._secondPoke.getCurrentHealth() == 0 ) and ( trainer._thirdPoke.getCurrentHealth() == 0 ) and ( trainer._fourthPoke.getCurrentHealth() == 0 ):
            #print(f"{trainer._currentPoke.getName()} fainted!")
            trainer.setStatus(False)
            return
            
        elif trainer._currentPoke.getCurrentHealth() == 0:
            #print(f"{trainer._currentPoke.getName()} fainted!")
            for pokemon in trainer.getPokemons():
                if pokemon.getCurrentHealth()>0:
                    trainer.setCurrentPoke(pokemon)
                    print(f"{trainer.getName()} uses {trainer._currentPoke.getName()}!")
                    print("")
                    break
    def showHP(self, trainer):
        print(f"{trainer._currentPoke.getName()} has {trainer._currentPoke.getCurrentHealth()} health left out of {trainer._currentPoke.getMaxHealth()}")
        
#modify so you can choose any of the 4 pokemons        
    def changePokemon(self, trainer):
        UserInput = input(f"{trainer.getName()}, do you wish to change your pokemon? If yes, type !: ")
        if UserInput == "!":
            print(trainer._firstPoke.getName(), "," , trainer._secondPoke.getName(),"," ,trainer._thirdPoke.getName(),"," ,trainer._fourthPoke.getName())
            try:
                UserInput2 = int(input(f"{trainer.getName()}, input 1, 2,3,4 for the corresponding pokemon you want to change to:"))
                if trainer.getPokemons()[UserInput2 - 1].getCurrentHealth() == 0:
                    print("That pokemon already fainted!")
                else:
                    trainer.setCurrentPoke(trainer.getPokemons()[UserInput2 - 1])                                                      
                    print(f"{trainer.getName()} uses {trainer._currentPoke.getName()}!")  
                    print("")
            except IndexError:
                print("Type in a valid number")
            except ValueError: 
                print("Type in a valid number")                
              
    def choosePokemon(self, trainer1, trainer2, p1Pokemons, p2Pokemons): #last two are lists
        
        self.choosePokemonOrder(trainer1, p1Pokemons)
        print("")
        self.choosePokemonOrder(trainer2, p2Pokemons)
        print("")
        print(f"{trainer1.getName()} sends out {trainer1._currentPoke.getName()}!")                                                                                                              
        print(f"{trainer2.getName()} sends out {trainer2._currentPoke.getName()}!") 
           
    def battle(self, trainer1, trainer2): 
        
        while (trainer1.getStatus() == True) and (trainer2.getStatus() == True) :   
                                          
            speed1 = trainer1._currentPoke.getSpeed()                                              
            speed2 = trainer2._currentPoke.getSpeed()
                                                                                                                                                                                                                                              
            if self.compareSpeeds(speed1, speed2) == True:
                p1Move, p1Dmg = self.chooseMove(trainer1)                            
                print(f"{trainer1._currentPoke.getName()} attacks first!")                                 
                print(f"{trainer1._currentPoke.getName()} uses {p1Move}")                                                                                                                                                                                                                                                    
                print(trainer2._currentPoke.takeDmg(p1Dmg , trainer1._currentPoke))
                self.showHP(trainer2)
                print("") 
                self.checkAlive(trainer2) 
                p2Move, p2Dmg = self.chooseMove(trainer2)
                print(f"{trainer2._currentPoke.getName()} uses {p2Move}") 
                print(trainer1._currentPoke.takeDmg(p2Dmg , trainer2._currentPoke))
                self.checkAlive(trainer1)
                self.showHP(trainer1)
                #Asking trainers if they want to switch pokemons 
                self.changePokemon(trainer1)
                self.changePokemon(trainer2)
                
            else:
                p2Move, p2Dmg = self.chooseMove(trainer2) 
                print(f"{trainer2._currentPoke.getName()} attacks first!")    
                print(f"{trainer2._currentPoke.getName()} uses {p2Move}")
                print(trainer1._currentPoke.takeDmg(p2Dmg , trainer2._currentPoke))
                self.showHP(trainer1)
                print("")
                self.checkAlive(trainer1)
                
                p1Move, p1Dmg = self.chooseMove(trainer1)
                print(f"{trainer1._currentPoke.getName()} uses {p1Move}") 
                print(trainer2._currentPoke.takeDmg(p1Dmg , trainer1._currentPoke))
                self.checkAlive(trainer2)
                self.showHP(trainer2)
                #Asking trainers if they want to switch pokemons 
                self.changePokemon(trainer2)
                self.changePokemon(trainer1)
                
        #once the battle has ended:        
        if trainer1.getStatus() == False:
            print(f"{trainer2.getName()} wins the battle!")
        elif trainer2.getStatus() == False:
            print(f"{trainer1.getName()} wins the battle!")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                          
                          
         
                                                                                                                                                                        
                          
                      
                      
                          
                      
                      
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                       
        