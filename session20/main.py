# task manager-> function
# class => blue print
# object, instance
# property: variable
# method: function


class Car:
    def __init__(
            self, 
            color:str, 
            brand:str, 
            model:int, 
            h_speed:int, 
            speed:int
        ):
        
        self.color = color
        self.brand = brand
        self.model = model
        self.h_speed = h_speed
        self.speed = speed
        
        print(f'the {self.color} {self.brand} is created')

    def increase_speed(self, amount:int = 0):
        self.speed += amount
        print(self.speed)
    
    def get_speed(self):
        return self.speed
        



class Truck(Car):
    pass




c1 = Car('blue', 'pego', 2026, 300, 30)
c2 = Car('red', 'benz', 2024, 200, 60)

