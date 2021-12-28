class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed=speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print ('Pojehali')

    def stop(self):
        print ("Ostanovis")

    def turn(self,direction):
        print('Povorot',direction)

    def show_speed(self):
        print ("Skorost", self.speed)

class TownCar(Car):
    def show_speed (self):
        super()._show_speed()
        if self.speed>60:
            print ("Pevishenije")

class WorkCar(Car):
    def show_speed (self):
        super()._show_speed()
        if self.speed>40:
            print ("Pevishenije")

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name,True)

obj1 = TownCar(50,'green',"Town")
obj2=SportCar(190,'red','Sport')
obj3 = WorkCar(25,'grey',"work")
obj4=PoliceCar(90,'blue','police')

obj1.show_speed()
obj3.show_speed()

obj3.speed=50
obj3.show_speed()

obj4.turn('Left')
