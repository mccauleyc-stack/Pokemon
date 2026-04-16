'''
Created on Sep 25, 2025

@author: mccauleyc
'''
import random
from abc import abstractmethod
class Pokemon():

    #constructor magic functions
    def __init__(self, name, level = 1):
        self._name = name
        self._level = level
        self._maxHealth = 1
        self._currentHealth = self._maxHealth
        self._speed = 1
        self._weakness = []
        self._strength = []
    
        self._attackNames = [] #parrallel lists
        self._attackDmg = []
        
    #toString
    def __str__(self):
        return f"{self._name}  {self._level}"
    
    def printName(self ):
        print(self._name)

        #getters
    def getName(self):
        return self._name

    @abstractmethod
    def getType(self):
        pass
    
    def getLevel(self):
        return self._level
    def getMaxHealth(self):
        return self._maxHealth
    def getCurrentHealth(self):
        return self._currentHealth
    def getSpeed(self):
        return self._speed
    def getWeakness(self):
        return self._weakness
    def getStrength(self):
        return self._strength
        
    def getAttackNames(self):
        return self._attackNames
    
    def getAttackDmg(self):
        return self._attackDmg
    
    
        #setters
    def setName(self, name):
        self._name = name
    def setLevel(self, level):
        self._level = level
    def setPokeType(self, pokeType):
        self._pokeType = pokeType
    def setMaxHealth(self, maxHealth):
        self._maxHealth = maxHealth
    def setCurrentHealth(self, health):
        self._currentHealth = health
    def setSpeed(self, speed):
        self._speed = speed
        
        
        
    def addWeakness(self, weakness):
        self._weakness.append(weakness)
    def addStrength(self, strength):
        self._strength.append(strength)    

    def slow(self, slow):
        self._speed -= slow
    def levelUp(self):
        self._level += 1
        self._maxHealth *= 1.2 
        self._speed += 1
    def confused(self):
        randomAttack = random.randint(0, len(self._attackNames))
        return self._attackNames[randomAttack], self._attackDmg[randomAttack] 
    
    #your damage should have a 2x multiplier if you are weak to it
    #your damage should have a 1/2x multiplier if you are strong to it
    #include evasion
    #return damage done
    #attacktingType is expected a string
    #use a getter getType to get the string
    @abstractmethod    
    def takeDmg(self, dmg, attackingType):
        pass