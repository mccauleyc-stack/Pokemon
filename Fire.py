'''
Created on May 4, 2026

@author: julianbarroso
'''
import random                                                                                                                    
from PokemonClass import Pokemon                                                                                                 
class Fire(Pokemon):                                                                                                             
    def __init__(self, name, maxHP, speed, attack, specialAttack, defense, specialDefense, description):             
        super().__init__(name, maxHP, speed, attack, specialAttack, defense, specialDefense, description)            
                                                                                                                                 
        self._doubleDamageTo = ["Bug", "Steel", "Grass", "Ice"]                                                                                                 
        self._halfDamageTo = ["Rock", "Fire", "Water", "Dragon"]                                                                                                   
        self._noDamageTo = []                                                                                                    
                                                                                                                                 
        self._doubleDamageFrom = ["Ground", "Rock", "Water"]                                                                                                
        self._halfDamageFrom = ["Bug", "Steel", "Fire","Grass", "Ice", "Fairy"]                                                                                                  
        self._noDamageFrom = []                                                                                                  
                                                                                                                                 
    #toString                                                                                                                    
    def __str__(self):                                                                                                           
        return f"{self._name}, {self._level}, Fire"                                                                              
                                                                                                                                 
    #getters                                                                                                                     
    def getDoubleDamageTo(self):                                                                                                 
        return self._doubleDamageTo                                                                                              
    def getHalfDamageTo(self):                                                                                                   
        return self._halfDamageTo                                                                                                
    def getNoDamageTo(self):                                                                                                     
        return self._noDamageTo                                                                                                  
    def getDoubleDamageFrom(self):                                                                                               
        return self._doubleDamageFrom                                                                                            
    def getHalfDamageFrom(self):                                                                                                 
        return self._halfDamageFrom                                                                                              
    def getNoDamageFrom(self):                                                                                                   
        return self._noDamageFrom                                                                                                
    def getType(self):                                                                                                           
        return "Fire"                                                                                                            
                                                                                                                                 
    #setters                                                                                                                     
    def setDoubleDamageTo(self, newDoubleDamageTo):                                                                              
        self._doubleDamageTo = newDoubleDamageTo                                                                                 
    def setHalfDamageTo(self, newHalfDamageTo):                                                                                  
        self._halfDamageTo = newHalfDamageTo                                                                                     
    def setNoDamageTo(self, newNoDamageTo):                                                                                      
        self._noDamageTo = newNoDamageTo                                                                                         
    def setDoubleDamageFrom(self, newDoubleDamageTo):                                                                            
        self._doubleDamageFrom = newDoubleDamageTo                                                                               
    def setHalfDamageFrom(self, newHalfDamageFrom):                                                                              
        self._halfDamageFrom = newHalfDamageFrom                                                                                 
    def setNoDamageFrom(self, newNoDamageFrom):                                                                                  
        self._noDamageFrom = newNoDamageFrom                                                                                     
                                                                                                                                 
    #helperFunctions                                                                                                             
    def takeDmg(self, dmg, attacker): #change function                                                                           
        attackingType = attacker.getType()                                                                                       
                                                                                                                                 
        if (random.randint(1,20) == 1):                                                                                          
            return f"{self._name} evaded the attack!"                                                                            
                                                                                                                                 
        elif (attackingType in self._weaknesses):                                                                                
            self._currentHealth -= (dmg*2)                                                                                       
            self._currentHealth = round(self._currentHealth)                                                                     
            if (self._currentHealth <= 0):                                                                                       
                self.setCurrentHealth(0)                                                                                         
                return f"{attacker.getName()}'s attack was super effective! \n{self._name} fainted!"                             
            return f"{attacker.getName()}'s attack was super effective!"                                                         
                                                                                                                                 
        elif (attackingType in self._strengths):                                                                                 
            self._currentHealth -= (dmg*0.5)                                                                                     
            self._currentHealth = round(self._currentHealth)                                                                     
            if (self._currentHealth <= 0):                                                                                       
                self.setCurrentHealth(0)                                                                                         
                return f"{attacker.getName()}'s attack was not very effective! \n{self._name} fainted!"                          
            return f"{attacker.getName()}'s attack was not very effective!"                                                      
                                                                                                                                 
        else:                                                                                                                    
            self._currentHealth -= dmg                                                                                           
            self._currentHealth = round(self._currentHealth)                                                                     
            if (self._currentHealth <= 0):                                                                                       
                self.setCurrentHealth(0)                                                                                         
                return f"{self._name} took {dmg} damage. \n{self._name} fainted!."                                               
            return f"{self._name} took {dmg} damage."                                                                            