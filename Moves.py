class Moves():

    def __init__(self, name, accuracy, powerPoints, power, moveType, description, damageType):

        self._name = name #string

        self._accuracy = accuracy #float

        self._powerPoints = powerPoints #integer

        self._power = power #integer
        
        self._type = moveType #string
        
        self._damageType = damageType #string
        
        self._description = description #string
        
    #toString
    def __str__(self):
        return f"{self._name}, {self._moveType}"
        
    #getters
    def getName(self):
        return self._name
    def getAccuracy(self):
        return self._accuracy
    def getPowerPoints(self):
        return self._powerPoints
    def getPower(self):
        return self._power
    def getType(self):
        return self._moveType
    def getDamageType(self):
        return self._damageType
    def getDescription(self):
        return self._description
    
    #setters
    def setName(self, newName):
        self._name = newName
    def setAccuracy(self, newAccuracy):
        self._accuracy = newAccuracy
    def setPowerPoints(self, newPowerPoints):
        self._powerPoints = newPowerPoints
    def setPower(self, newPower):
        self._power = newPower
    def setType(self, newType):
        self._type = newType
    def setDamageType(self, newDamageType):
        self._damageType = newDamageType
    def setDescription(self, newDescription):
        self._description = newDescription
    
    #helper functions
