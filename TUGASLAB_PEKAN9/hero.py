class Human:
    def __init__(self,name,position):
        self.name = name
        self.__position = position
        self.speed = 1
        
    def getPosition(self):
        return self.__position
    
    def movement(self, arah):
        if arah == 'L':
            self.__position -= self.speed
        elif arah == 'R':
            self.__position += self.speed 
    
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
        
class Assassin(Hero):
    def __init__(self, name, position) :
        super().__init__(name, position)
        self._power = 35
        self.speed = 4
    
    def attack(self, target):
        target._health -= self._power

    def special(self, target):
        self.speed = 7
        self._power = 42
        target._health -= self._power      

    def getHealth(self):
        return self._health
    
    def getSpeed(self):
        return self.speed
    
        
class Warrior(Hero):
    def __init__(self, name, position) :
        super().__init__(name, position)
        self._armor = 30
        self._power = 26
    
    def attack(self, target):
        target._health -= self._power
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power 
        
    def getHealth(self):
        return self._health
        

class Support(Hero):
    def __init__(self, name, position) :
        super().__init__(name, position)
        self._health = 500
        self._power = 8
        self.speed = 4
    
    def special(self, target):
        self.speed = 6
        target._health += 150
        
    def getHealth(self):
        return self._health
    
    def getSpeed(self):
        return self.speed
    
        