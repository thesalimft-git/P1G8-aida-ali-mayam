# oop: design pattern
# function base: main, menu, function

# class: blueprint, map
# object, instance: 
# method: function, 
# property, attribute: variable
# inheritance: 
# abstraction: 
# polymorphism: 
# encapsulation:



u1_name = 'sali'
u1_health = 90
u1_gun = 10
u1_speed = 80

u2_name = 'maryam'
u2_health = 95
u2_gun = 15
u2_speed = 70

u3_name = 'ayda'
u3_health = 90
u3_gun = 10
u3_speed = 80

u4_name = 'ali'
u4_health = 100
u4_gun = 5
u4_speed = 100

u4_name = 'aten'
u4_health = 100
u4_gun = 5
u4_speed = 100



def echo_health(name: str) -> int:
    match name:
        case 'sali':
            return u1_health
        case 'maryam':
            return u2_health
        case 'aida':
            return u3_health
        case 'ali':
            return u4_health



def shoot(killer, victim, amount):
    match killer:
        case 'sali':
            u1_health += 5
            match victim:
                case 'sali':
                    print('error')
                case 'maryam':
                    u2_health -= 10
                case 'aida':
                    u3_health -= 10
                case 'ali':
                    u4_health -= 10
        case 'maryam':
            case 
            
            
            

class Player:
    def __init__(self, name, health, gun, speed) -> None:
        self.name = name
        self.health = health
        self.gun = gun
        self.speed = speed
        print('object created')
        
    def echo_health(self):
        return self.health
    
    def shoot(self, target):
        self.health += 5
        target.health -= 10
        
class ProPlayer(Player) :
    pass




sali = Player(
    name= 'sali',
    health= 80,
    gun= 10,
    speed= 90,
)
aida = Player(
    name= 'aida',
    health= 90,
    gun= 10,
    speed= 100,
)


sali.shoot(aida)


maryam = ProPlayer()

