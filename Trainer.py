class Trainer():
    def __init__(self, name, poke1, poke2,poke3,poke4, status = True):
        self._name = name
        self._firstPoke = poke1
        self._secondPoke = poke2
        self._currentPoke = poke1
        self._status = status
        self._pokemons = [poke1, poke2, poke3,poke4]#list
        self._thirdPoke= poke3
        self._fourthPoke= poke4
        
        
    def getFirstPoke(self):
        return self._firstPoke
    def getSecondPoke(self):
        return self._secondPoke
    def getThirdPoke(self):
        return self._thirdPoke   
    def getFourthPoke(self):
        return self._fourthPoke
    def getName(self):
        return self._name
    def getCurrentPoke(self):
        return self._currentPoke
    def getStatus(self):
        return self._status
    def getPokemons(self):
        return self._pokemons 
    
    def setFirstPoke(self, poke):
        self._firstPoke = poke
        self._pokemons[0]=poke
    def setSecondPoke(self, poke):
        self._secondPoke = poke
        self._pokemons[1]=poke
    def setThirdPoke(self, poke):
        self._thirdPoke = poke
        self._pokemons[2]=poke
    def setFourthPoke(self, poke):
        self._fourthPoke = poke
        self._pokemons[3]=poke
    def setName(self, name):
        self._name = name
    def setCurrentPoke(self, poke):
        self._currentPoke = poke
    def setStatus(self, newStatus):
        self._status = newStatus

        
        
    
