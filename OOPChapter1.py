class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount
    
    def get_damage(self, amount):
        self.health -= amount
    
    def weapon_status(self):
        print ('I am without a weapon !! :-( ')
        
class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

    def speed(self):
        print('I am moving at the speed of')

class Shark:
    def bite(self):
        print('The Shark has bitten')

monster = Monster(100, 100)
print(monster.health)
hero = Hero(15, monster)
hero.attack()
print(monster.health)    
