
class Moves():
    def __init__(self, name, accuracy, pp, power, damageType, description, moveType):
        self._name = name
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = moveType
        self._description = description
        self._damageType = damageType
    def getName(self):
        return self._name
    def getAccuracy(self):
        return self._accuracy
    def getPP(self):
        return self._pp
    def decreasePP(self):
        if self._pp == 0:
            self._pp = 0
        else:
            self._pp = self._pp - 1
    def getPower(self):
        return self._power
    def getmoveType(self):
        return self._type
    def getDescription(self):
        return self._description
    def getDamageType(self):
        return self._damageType

