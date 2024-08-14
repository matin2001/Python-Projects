import geometry


print("Learn Geometry.")
print("  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter")
print("  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program")
loop = True
Shape = geometry.Shapelist()
number_of_Shapes = 0
perimeter = []
area = []
while(loop == True):
    order = int(input())
    if (order == 1): # for adding every shape to the list of our shapes, we enter 1 and after that choose the number
                     # of the shape we want to define and then, we should enter the sides that are asked
        number_of_Shapes = number_of_Shapes + 1
        print("List of shapes: 1.Circle  2.Triangle  3.Equilateral_triangle  4.Rectangle  5.Square  6.Regular_pantagon")
        number = int(input())
        if(number == 1):
            print("Enter radius:")
            r = int(input())
            Shape.add_shape(geometry.Circle(r))
        if (number == 2):
            print("Enter a, b, c")
            a = int(input())
            b = int(input())
            c = int(input())
            Shape.add_shape(geometry.Triangle(a, b, c))
        if (number == 3):
            print("Enter a:")
            a = int(input())
            Shape.add_shape(geometry.Equilateral_triangle(a))
        if (number == 4):
            print("Enter a, b")
            a = int(input())
            b = int(input())
            Shape.add_shape(geometry.Rectangle(a, b))
        if (number == 5):
            print("Enter a:")
            a = int(input())
            Shape.add_shape(geometry.Square(a))
        if (number == 6):
            print("Enter a:")
            a = int(input())
            Shape.add_shape(geometry.Regular_pantagon(a))
    if (order == 2): # print the markdown table
        print(Shape.get_shapes_table())
    if (order == 3):
        print(perimeter)
    if (order == 4):
        pass
    if (order == 5): # for getting the formula of every shape first we enter 4 and then enter the number of the
                     # shape to see the formulas
        print("List of shapes: 1.Circle  2.Triangle  3.Equilateral_triangle  4.Rectangle  5.Square  6.Regular_pantagon")
        number = int(input())
        if (number == 1):
            print("Perimeter : " , geometry.Circle.get_perimeter_formula())
            print("Area : " , geometry.Circle.get_area_formula())
        if (number == 2):
            print("Perimeter : " , geometry.Triangle.get_perimeter_formula())
            print("Area : " , geometry.Triangle.get_area_formula())
        if (number == 3):
            print("Perimeter : " , geometry.Equilateral_triangle.get_perimeter_formula())
            print("Area : " , geometry.Equilateral_triangle.get_area_formula())
        if (number == 4):
            print("Perimeter : " , geometry.Rectangle.get_perimeter_formula())
            print("Area : " , geometry.Rectangle.get_area_formula())
        if (number == 5):
            print("Perimeter : " , geometry.Square.get_perimeter_formula())
            print("Area : " , geometry.Square.get_area_formula())
        if (number == 6):
            print("Perimeter : " , geometry.Regular_pantagon.get_perimeter_formula())
            print("Area : " , geometry.Regular_pantagon.get_area_formula())
    if (order == 0):
        break
    print("  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter")
    print("  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program")

