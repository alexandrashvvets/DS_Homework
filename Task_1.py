from time import sleep

class TrafficLight:
    color =('red', 'yellow','green')
    rejim = (7,2,5)

    def __init__(self):
        self.__color='green'

    def running (self):
        while True:
            for i in self.__color:
                self.__color=i
                print (self.__color)
                sleep(self.rejim[self.color.index(self.__color)])

light = TrafficLight
light.running()