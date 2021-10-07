#pascal naming convention
class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


#creating object
point1 = Point(10,20)
#point1.x = 10;
print(point1.x)
point1.draw()

