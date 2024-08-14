import math


class Shape:
    #this is a abstract class that other classes are inherrited from it
    def get_area(self):
        """In every class that is inherrited from class Shape we define this function for getting area of the shape
            and the formula differs in every class
            :return area of the shape
        """
        pass
    def get_perimeter(self):
        """In every class that is inherrited from class Shape we define this function for getting perimeter of the shape
            and the formula differs in every class
            :return perimeter of the shape
        """
        pass
    def __str__(self):
        """In every class that is inherrited from class Shape we define this function for getting the information of the shape
            and the formula differs in every class
            :return name of the shape and size of the side
        """
        pass
    @classmethod
    def check_if_args_not_below_zero(cls, *args):
        """checks the arguments we enter if they are bigger than 0 or not"""
        for arg in args:
            if (arg < 0):
                raise ValueError("Input should be correct")
        return True

    @classmethod
    def get_area_formula(cls):
        """The function gives us the formula which calculates the area of the shape and differs in every class"""
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """The function gives us the formula which calculates the area of the shape and differs in every class"""
        pass

# we define 6 classes and in every class override the functions above
class Circle(Shape):
    def __init__(self, r):
        self.check_if_args_not_below_zero(r)
        self.r = r
    def get_area(self):
        return math.pi * self.r * self.r
    def get_perimeter(self):
        return 2 * math.pi * self.r
    def __str__(self):
        return f'Circle, r = {self.r}'

    @classmethod
    def get_area_formula(cls):
        return "pi * r * r"
    @classmethod
    def get_perimeter_formula(cls):
        return "pi * r * 2"

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.check_if_args_not_below_zero(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        S = math.sqrt(s)
        return S
    def get_perimeter(self):
        return self.a + self.b + self.c
    def __str__(self):
        return f'Triangle, a = {self.a}, b = {self.b}, c = {self.c}'
    @classmethod
    def get_area_formula(cls):
        return "Heron Formula : p = (a + b + c)/2 , S = p * (p - a) * (p - b) * (p - c)"
    @classmethod
    def get_perimeter_formula(cls):
        return "a + b + c"


class Equilateral_triangle(Triangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
        self.c = a

    def __str__(self):
        return f'Equilateral Triangle, a = {self.a}'


class Rectangle(Shape):
    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b
    def get_area(self):
        S = self.a * self.b
        return S
    def get_perimeter(self):
        return 2*(self.a + self.b)
    def __str__(self):
        return f'Rectangle, a = {self.a}, b = {self.b}'
    @classmethod
    def get_area_formula(cls):
        return "a * b"
    @classmethod
    def get_perimeter_formula(cls):
        return "2 * (a + b)"


class Square(Rectangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
    def __str__(self):
        return f'Square, a = {self.a}'

class Regular_pantagon(Shape):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
    def get_area(self):
        s1 = (5+2*math.sqrt(5))
        S = (1/4)*math.sqrt(5*s1)*self.a*self.a
        return S
    def get_perimeter(self):
        return (5 * self.a)
    def __str__(self):
        return f'Regular Pantagon, a = {self.a}'
    @classmethod
    def get_area_formula(cls):
        return "(1/4)* math.sqrt( 5 * (5 + 2 * math.sqrt(5))) * a * a"
    @classmethod
    def get_perimeter_formula(cls):
        return "5 * a"

class Shapelist:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        """for adding every shape to list of our shapes we call this function"""
        if not (isinstance(shape, Shape)):
            raise TypeError
        self.shapes.append(shape)

    def get_shapes_table(self):
        """this function gives us a markdown table from the shapes that are defined"""
        a = "| idx |   Class  |     __str__     |  Perimeter  |  Formula  |\n"
        a = a + "| --- | -------- | --------------- | ----------- | --------- |\n"
        length = len(self.shapes)
        i = 0
        while(i < length):
            a = a + "|  " + str(i) + "  |  "
            if (type(self.shapes[i]) == Circle):
                a = a + "Circle"
            if (type(self.shapes[i]) == Rectangle):
                a = a + "Rectangle"
            if (type(self.shapes[i]) == Triangle):
                a = a + "Triangle"
            if (type(self.shapes[i]) == Square):
                a = a + "Square"
            if (type(self.shapes[i]) == Equilateral_triangle):
                a = a + "Equilateral Triangle"
            if (type(self.shapes[i]) == Regular_pantagon):
                a = a + "Regular Pantagon"
            a = a + "  |  " + self.shapes[i].__str__()
            a = a + "  |    " + str(self.shapes[i].get_perimeter()) + "    |   " + self.shapes[i].get_area_formula() + "\n"
            i = i + 1
        return a

