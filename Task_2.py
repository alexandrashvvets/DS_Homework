class Road:
    def __init__(self,length,width ):
        self._length=length
        self._width=width

    def get_weight (self, massa, dlina):
        return self._length*self._width*massa*dlina/1000


road = Road (100000,20)
print(road.get_weight(15,6))