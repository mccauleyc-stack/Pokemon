'''
Created on Sep 25, 2025

@author: mccauleyc
'''
import random
from abc import abstractmethod
class Pokemon():

    #constructor magic functions
    def __init__(self, name, maxHP, speed, attack, specialAttack, defense, specialDefense, description):
        self._name = name
        self._maxHP = maxHP
        self._speed = speed
        self._attack = attack
        self._specialAttack = specialAttack
        self._defense = defense
        self._specialDefense = specialDefense
        self._moves = [] #list
        self._description = description
        
        self._currentHP = self._maxHP
        self._level = 1 
         
    #toString  
    def __str__(self):
        return f"{self._name},  {self._level}"
    
    def printName(self):
        print(self._name)

        #getters
    def getName(self):
        return self._name 
    def getMaxHP(self):
        return self._maxHP
    def getSpeed(self):
        return self._speed 
    def getAttack(self):
        return self._attack
    def getSpecialAttack(self):
        return self._specialAttack
    def getDefense(self):
        return self._defense
    def specialDefense(self):
        return self._specialDefense
    def getMoves(self): #returns list    
        return self._moves                                    
    def getCurrentHP(self):     
        return self._currentHP  
    def getLevel(self):    
        return self._level 
    @abstractmethod   
    def getType(self):
        pass 
    @abstractmethod 
    def getWeaknesses(self):   
        pass
    @abstractmethod   
    def getStrengths(self):    
        pass      
    def getDescription(self):
        return self._description
         
    
        #setters
    def setName(self, newName):
        self._name = newName
    def setMaxHP(self, newMaxHP): 
        self._maxHP = newMaxHP       
    def setSpeed(self, newSpeed): 
        self._speed = newSpeed       
    def setAttack(self, newAttack):
        self._attack = newAttack
    def setSpecialAttack(self, newSpecialAttack):   
        self._speicalAttack = newSpecialAttack
    def setDefense(self, newDefense):
        self._defense = newDefense
    def setSpecialDefense(self, newSpecialDefense):
        self._specialDefense = newSpecialDefense
    def setMoves(self, moves):                                        
        self._moves = moves #moves should be a list of four objects                                                                 
    def setCurrentHP(self, newCurrentHP): 
        self._currentHP = newCurrentHP       
    def setLevel(self, newLevel):
        self._level = newLevel
    def setDescription(self, newDescription):
        self._description = newDescription
        
        #helper functions   
    def slow(self, slow): #change this function
        self._speed -= slow
        
    def levelUp(self): 
        self._level += 1
        self._maxHealth *= 1.2 
        self._speed += 1
        
    def confused(self): #change this function
        randomAttack = random.randint(0, len(self._attackNames))
        return self._attackNames[randomAttack], self._attackDmg[randomAttack] 
    
    #your damage should have a 2x multiplier if you are weak to it
    #your damage should have a 1/2x multiplier if you are strong to it
    #include evasion
    #return damage done
    #attacktingType is expected a string
    #use a getter getType to get the string
    @abstractmethod    
    def takeDmg(self, dmg, attackingType): #change function
        pass