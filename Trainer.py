class Trainer():
    def __init__(self, name, pokemon): #pokemon is a list of 6 pokemon
        self._name = name
        self._pokemon = pokemon
        self._currentPokemon = pokemon[0]
        self._status = True
        
        #toString                                     
    def __str__(self):                            
        return f"{self._name},  {self._pokemon}"       
        
        #getters
    def getName(self):   
        return self._name   
    def getPokemon(self):
        return self._pokemon #list of 6
    def getCurrentPokemon(self):
        return self._currentPokemon
    def getStatus(self):
        return self._status
    def getFirstPokemon(self):  
        return self._pokemon[0]      
    def getSecondPokemon(self):    
        return self._pokemon[1]     
    def getThirdPokemon(self):     
        return self._pokemon[2]      
    def getFourthPokemon(self):    
        return self._pokemon[3]      
    def getFifthPokemon(self):     
        return self._pokemon[4]     
    def getSixthPokemon(self):     
        return self._pokemon[5]      
                                            
     
        
        #setters
    def setName(self, name):                           
        self._name = name                              
    def setPokemon(self, newPokemon):                  
        self._pokemon = newPokemon                     
    def setCurrentPokemon(self, newCurrentPokemon):    
        self._currentPokemon = newCurrentPokemon       
    def setStatus(self, newStatus): #boolean           
        self._status = newStatus                           
   
    def setFirstPokemon(self, newPokemon):
        self._pokemon[0] = newPokemon
    def setSecondPokemon(self, newPokemon):
        self._pokemon[1] = newPokemon
    def setThirdPokemon(self, newPokemon):
        self._pokemon[2] = newPokemon
    def setFourthPokemon(self, newPokemon):
        self._pokemon[3] = newPokemon
    def setFifthPokemon(self, newPokemon):
        self._pokemon[4] = newPokemon  
    def setSixthPokemon(self, newPokemon):   
        self._pokemon[5] = newPokemon  
    
    #helperFunctions




        
        
    
