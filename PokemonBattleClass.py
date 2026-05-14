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
    
    #helperFunctions
    def choosePokemon(self, trainer1, trainer2):        
                                                                                                    
        self.choosePokemonOrder(trainer1)                                               
        print("")                                                                            
        self.choosePokemonOrder(trainer2)                                               
        print("")                                                                                   
        print(f"{trainer1.getName()} sends out {trainer1.getCurrentPokemon().getName()}!")                 
        print(f"{trainer2.getName()} sends out {trainer2.getCurrentPokemon().getName()}!")                                                                                                                 
          
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
                print(f"{trainer.getCurrentPokemon().getMoves()}")                                      
                #talk to Josue, add code here based on that
                               
    def checkAlive(self, trainer):
        if ( trainer.getFirstPokemon().getCurrentHP() == 0 ) and ( trainer.getSecondPokemon().getCurrentHP() == 0 ) and ( trainer.getThirdPokemon().getCurrentHP() == 0 ) and ( trainer.getFourthPokemon().getCurrentHP() == 0 ) and ( trainer.getFifthPokemon().getCurrentHP() == 0 ) and ( trainer.getSixthPokemon().getCurrentHP() == 0 ):
            print(f"{trainer.getCurrentPokemon().getName()} fainted!")
            trainer.setStatus(False)
            return
        elif ( trainer.getCurrentPokemon().getCurrentHP() == 0 ):
            print(f"{trainer.getCurrentPokemon().getName()} fainted!")
            for pokemon in trainer.getPokemon():
                if pokemon.getCurrentHealth() > 0:
                    trainer.setCurrentPokemon(trainer.getPokemon()[pokemon])
                    print(f"{trainer.getName()} uses {trainer.getCurrentPokemon().getName()}!")
                    print("")
                    break
            
    def showHP(self, trainer):
        print(f"{trainer.getCurrentPokemon().getName()} has {trainer.CurrentPokemon().getCurrentHP()} out of {trainer.getCurrentPokemon.getMaxP()} health left!")
        
    #does not work, will modify with GUIs 
    def changePokemon(self, trainer): 
        #will add code based on GUIs
    
    #does not work         
    def battle(self, trainer1, trainer2): 
        
        while (trainer1.getStatus() == True) and (trainer2.getStatus() == True) :   
                                          
            speed1 = trainer1.getCurrentPokemon().getSpeed()                                              
            speed2 = trainer2.getCurrentPokemon().getSpeed()
                                                                                                                                                                                                                                              
            if self.compareSpeeds(speed1, speed2) == True:
                p1Move, p1Dmg = self.chooseMove(trainer1)                            
                print(f"{trainer1._currentPoke.getName()} attacks first!")                                 
                print(f"{trainer1._currentPoke.getName()} uses {p1Move}")                                                                                                                                                                                                                                                    
                print(trainer2.getCurrentPokemon().takeDmg(p1Dmg , trainer1.getCurrentPokemon()))
                self.showHP(trainer2)
                print("") 
                self.checkAlive(trainer2) 
                p2Move, p2Dmg = self.chooseMove(trainer2)
                print(f"{trainer2.getCurrentPokemon().getName()} uses {p2Move}") 
                print(trainer1.getCurrentPokemon().takeDmg(p2Dmg , trainer2.getCurrentPokemon()))
                self.checkAlive(trainer1)
                self.showHP(trainer1)
                #Asking trainers if they want to switch pokemon 
                self.changePokemon(trainer1)
                self.changePokemon(trainer2)
                
            else:
                p2Move, p2Dmg = self.chooseMove(trainer2) 
                print(f"{trainer2.getCurrentPokemon().getName()} attacks first!")    
                print(f"{trainer2.getCurrentPokemon().getName()} uses {p2Move}")
                print(trainer1.getCurrentPokemon().takeDmg(p2Dmg , trainer2.getCurrentPokemon()))
                self.showHP(trainer1)
                print("")
                self.checkAlive(trainer1)
                
                p1Move, p1Dmg = self.chooseMove(trainer1)
                print(f"{trainer1.getCurrentPokemon().getName()} uses {p1Move}") 
                print(trainer2.getCurrentPokemon().takeDmg(p1Dmg , trainer1.getCurrentPokemon()))
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                          
                          
         
                                                                                                                                                                        
                          
                      
                      
                          
                      
                      
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                       
        