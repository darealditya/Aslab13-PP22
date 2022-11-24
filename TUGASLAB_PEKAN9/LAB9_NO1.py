from hero import Warrior, Assassin, Support

warrior = Warrior("Alufeed", position=10)
assassin = Assassin("Lancetod", position=25)
support = Support("Angela",position=30)

# sebelum
print(warrior.name)
print("health (before)", warrior.getHealth())
print("position (before)", warrior.getPosition())
assassin.attack(warrior)
warrior.movement('L')
# sesudah
print("health (after)", warrior.getHealth())
print("position (after)", warrior.getPosition())
print("-"*10)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
warrior.movement('R')
warrior.movement('R')
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())
print("Warrior (posisition):", warrior.getPosition())