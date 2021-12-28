class Stationery:
    def __init__(self,title ):
        self.title=title

    def draw(self):
        print ("Zapusk otrisovki")

class Pen(Stationery):
    def draw(self):
        print (f"Zapusk otrisovki pen, {self.title}")

class Pencil(Stationery):
    def draw(self):
        print (f"Zapusk otrisovki Pencil,{self.title}")

class Handle(Stationery):
    def draw(self):
        print (f"Zapusk otrisovki Handle,{self.title}")

p1 = Pen("Hey")
p2 = Pencil("2")
p3 = Handle("C")
p1.draw()
p2.draw()
p3.draw()