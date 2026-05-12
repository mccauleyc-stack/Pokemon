'''
Created on Jan 23, 2026

@author: julianbarroso
'''
import random
import copy

class Battle():
    def __init__(self, t1Pokemon, t2Pokemon):
        self._t1Pokemon = t1Pokemon #list of 6
        self._t2Pokemon = t2Pokemon #list of 6
    #getters    
    def getT1pokemon(self):
        return self._t1Pokemon #list
    def getT2pokemon(self):
        return self._t2Pokemon #list
    
    #setters 
    def setT1Pokemon(self, newPokemon): #list
        self._p1Pokemon = newPokemon        
    def setT2Pokemon(self, newPokemon): #list
        self._p2Pokemon = newPokemon
    
    #helper functions
    def choosePokemon(self, trainer1, trainer2):        
                                                                                                    
        self.choosePokemonOrder(trainer1)                                               
        print("")                                                                                   
        self.choosePokemonOrder(trainer2)                                               
        print("")                                                                                   
        print(f"{trainer1.getName()} sends out {trainer1.GetCurrentPokemon().getName()}!")                 
        print(f"{trainer2.getName()} sends out {trainer2.GetCurrentPokemon().getName()}!")                 
          
    #does not work, will modify with GUIs                                                                                                
    def choosePokemonOrder(self, trainer):
        pokemon = trainer.getPokemon()
      
        for i in range(6): #will run from 0 to 5 (# of pokemon)  
            inaccurate = False                                                                                                                                                      
            while inaccurate == False:                                                                                                                                              
                try:                                                                                                                                                                
                    number = int(input(f"{trainer.getName()}, what Pokemon will you use first? \nType 1 for {pokemon[0].getName()},\nor 2 for {pokemon[1].getName()},\nor 3 for {pokemon[2].getName()}, \nor 4 for {pokemon[3].getName()}, \nor 5 for {pokemon[4].getName()}, \nor 6 for {pokemon[5].getName()}: \n"))   
                    if number == 1:
                        inaccurate = True  
                    elif number == 2:
                        trainer.setCurrentPokemon(pokemon[1])                                                                                                                                                                                                                                    
                        inaccurate = True   
                    elif number == 3:
                        trainer.setCurrentPokemon(pokemon[2])     
                        inaccurate = True 
                    elif number == 4:   
                        trainer.setCurrentPokemon(pokemon[3]) 
                        inaccurate = True 
                    elif number == 5:                          
                        trainer.setCurrentPokemon(pokemon[4])     
                        inaccurate = True                      
                    elif number == 6:                          
                        trainer.setCurrentPokemon(pokemon[5]) 
                        inaccurate = True                                  
                except:
                    print("Please type either 1, 2, 3, 4, 5 or 6")                                                                                                                     
        
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
    #does not work, will modify with move class
    def chooseMove(self, trainer):                                                                           
            while True:     
                print("")                                                               
                print(f"{trainer.getName()}, what will {trainer.getCurrentPokemon().getName()} do?")         
                print(f"{trainer.getCurrentPokemon().getAttackNames()}")                                      
                try:                                                                                   
                    userInput = int(input("Type in 1, 2 or 3 for the corresponding moves:")) 
                    #Attack names no longer exists           
                    pokemonMove = trainer.getCurrentPokemon().getAttackNames()[userInput-1]  
                    #Get attack damage no longer exists                      
                    moveDmg = trainer.getCurrentPokemon().getAttackDmg()[userInput-1]
                    if (userInput == 1) or (userInput == 2) or (userInput == 3):                              
                        return pokemonMove, moveDmg                                                                                                                                                                 
                except IndexError:
                    print("Type in a valid number: 1, 2 or 3")
                except ValueError:
                    print("Type in a valid number: 1, 2 or 3")
                               
    def checkAlive(self, trainer):
        if ( trainer.getPokemon()[0].getCurrentHP() == 0 ) and ( trainer.getPokemon()[1].getCurrentHP() == 0 ) and ( trainer.getPokemon()[2].getCurrentHP() == 0 ) and ( trainer.getPokemon()[3].getCurrentHP() == 0 ) and ( trainer.getPokemon()[4].getCurrentHP() == 0 ) and ( trainer.getPokemon()[5].getCurrentHP() == 0 ):
            #print(f"{trainer._currentPokemon.getName()} fainted!")
            trainer.setStatus(False)
            return
        elif trainer.getCurrentPokemon().getCurrentHP() == 0:
            #print(f"{trainer._currentPokemon.getName()} fainted!")
            for pokemon in trainer.getPokemon():
                if pokemon.getCurrentHealth()>0:
                    trainer.setCurrentPoke(pokemon)
                    print(f"{trainer.getName()} uses {trainer.getCurrentPokemon().getName()}!")
                    print("")
                    break
            
    def showHP(self, trainer):
        print(f"{trainer.getCurrentPokemon().getName()} has {trainer.CurrentPokemon().getCurrentHP()} out of {trainer.getCurrentPokemon.getMaxP()} health left!")
        
    #does not work, will modify with GUIs 
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
     
     #does not work         
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
                #Asking trainers if they want to switch pokemon 
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
                #Asking trainers if they want to switch pokemon
                self.changePokemon(trainer2)
                self.changePokemon(trainer1)
                
        #once the battle has ended:        
        if trainer1.getStatus() == False:
            print(f"{trainer2.getName()} wins the battle!")
        elif trainer2.getStatus() == False:
            print(f"{trainer1.getName()} wins the battle!")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                          
                          
         
                                                                                                                                                                        
                          
                      
                      
                          
                      
                      
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                       
        