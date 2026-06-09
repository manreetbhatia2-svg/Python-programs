from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area():
        pass

class triangle(shape):
    def area(self,base,height):
        print(f"area of triangle is {0.5*base*height}")

class square(shape):
    def area(self,side):
        print(f"area of square is {side**2}")

TRIANGLE = triangle()
TRIANGLE.area(5,4)
TRIANGLE.area(10,14)

SQUARE = square()
SQUARE.area(7)

