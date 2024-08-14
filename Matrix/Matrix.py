class Integer:
    def __init__(self, value):
        if not (type(value) == int):
            raise TypeError("Input is not Correct")
        self.value = value

    def __add__(self, other):
        if (type(other) == Integer):
            self.value = self.value + other.value
            print(self.value)
        elif(type(other) == Complex):
            Complex.__add__(other, self)
        elif(type(other) == Matrix):
            Matrix.__add__(other, self)
        else:
            raise TypeError("Input is not Correct")

    def __sub__(self, other):
        if (type(other) == Integer):
            self.value = self.value - other.value
            print(self.value)
        elif(type(other) == Complex):
            Complex.__sub__(other, self)
        elif(type(other) == Matrix):
            Matrix.__sub__(other, self)
        else:
            raise TypeError("Input is not Correct")

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if (type(other) == Integer):
            a = Complex(other.value, 0)
            self.real = self.real + a.real
            self.imaginary = self.imaginary + a.imaginary
            print(self.real, "+", self.imaginary, "i", sep="")
        elif (type(other) == Complex):
            self.real = self.real + other.real
            self.imaginary = self.imaginary + other.imaginary
            print(self.real, "+", self.imaginary, "i", sep="")
        elif(type(other) == Matrix):
            Matrix.__add__(other, self)
        else:
            raise TypeError("Input is not Correct")


    def __sub__(self, other):
        if (type(other) == Integer):
            a = Complex(other.value, 0)
            self.real = self.real - a.real
            self.imaginary = self.imaginary - a.imaginary
            print(self.real, "+", self.imaginary, "i", sep="")
        elif (type(other) == Complex):
            self.real = self.real - other.real
            self.imaginary = self.imaginary - other.imaginary
            print(self.real, "+", self.imaginary, "i", sep="")
        elif(type(other) == Matrix):
            Matrix.__sub__(other, self)
        else:
            raise TypeError("Input is not Correct")



class Matrix:
    def __init__(self, row, column, numbers):
        self.row = row
        self.column = column
        self.numbers = []
        for i in range(column*row):
            if(type(numbers[i]) == int):
                a = numbers[i]
                self.numbers.append(Integer(a))
            else:
                a = numbers[i]
                num = a.split()
                real = int(num[0])
                b = num[2].split('i')
                imaginary = int(num[2][0])
                self.numbers.append(Complex(real, imaginary))

    def __add__(self, other):
        if(type(other) == Integer):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real + other.value
                elif (type(self.numbers[i]) == Integer):
                    self.numbers[i].value = self.numbers[i].value + other.value
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")
        elif(type(other) == Complex):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real + other.real
                    self.numbers[i].imaginary = self.numbers[i].imaginary + other.imaginary
                elif(type(self.numbers[i]) == Integer):
                    self.numbers[i] = Complex(self.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real + other.real
                    self.numbers[i].imaginary = self.numbers[i].imaginary + other.imaginary
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")
        elif(type(other) == Matrix):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex and type(other.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real + other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary + other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Complex and type(other.numbers[i]) == Integer):
                    other.numbers[i] = Complex(other.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real + other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary + other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Integer and type(other.numbers[i]) == Complex):
                    self.numbers[i] = Complex(self.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real + other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary + other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Integer and type(other.numbers[i]) == Integer):
                    self.numbers[i].value = self.numbers[i].value + other.numbers[i].value

            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")


    def __sub__(self, other):
        if(type(other) == Integer):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real - other.value
                elif (type(self.numbers[i]) == Integer):
                    self.numbers[i].value = self.numbers[i].value - other.value
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")
        elif(type(other) == Complex):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real - other.real
                    self.numbers[i].imaginary = self.numbers[i].imaginary - other.imaginary
                elif(type(self.numbers[i]) == Integer):
                    self.numbers[i] = Complex(self.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real - other.real
                    self.numbers[i].imaginary = self.numbers[i].imaginary - other.imaginary
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")
        elif(type(other) == Matrix):
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Complex and type(other.numbers[i]) == Complex):
                    self.numbers[i].real = self.numbers[i].real - other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary - other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Complex and type(other.numbers[i]) == Integer):
                    other.numbers[i] = Complex(other.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real - other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary - other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Integer and type(other.numbers[i]) == Complex):
                    self.numbers[i] = Complex(self.numbers[i].value, 0)
                    self.numbers[i].real = self.numbers[i].real - other.numbers[i].real
                    self.numbers[i].imaginary = self.numbers[i].imaginary - other.numbers[i].imaginary
                elif (type(self.numbers[i]) == Integer and type(other.numbers[i]) == Integer):
                    self.numbers[i].value = self.numbers[i].value - other.numbers[i].value
            for i in range(self.row * self.column):
                if (type(self.numbers[i]) == Integer):
                    print(self.numbers[i].value, end=" ")
                elif (type(self.numbers[i]) == Complex):
                    if (self.numbers[i].imaginary >= 0):
                        a = "+"
                    else:
                        a = "-"
                    print(self.numbers[i].real, a, self.numbers[i].imaginary, "i", sep="", end=" ")
                if ((i + 1) % self.column == 0):
                    print("")






    @staticmethod
    def make_unit_matrix(n):
        number = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                if(i == j):
                    a = Integer(1)
                    number[i][j] = a
                else:
                    a = Integer(0)
                    number[i][j] = a
         #this part is for printing the list
        for i in range(n):
            for j in range(n):
                print(number[i][j].value, end=" ")
            print("")


    @staticmethod
    def get_ith_row(matrix, i):
        col = matrix.column
        n = i * col
        for i in range(col):
            if(type(matrix.numbers[i+n]) == Integer):
                print(matrix.numbers[n+i].value, end=" ")
            elif(type(matrix.numbers[i+n]) == Complex):
                print(matrix.numbers[n+i].real, "+", matrix.numbers[n+i].imaginary, sep="",end="i ")
        print("")

    @staticmethod
    def get_ith_col(matrix, i):
        row = matrix.row
        column = matrix.column
        while(i < row * column):
            if(type(matrix.numbers[i]) == Integer):
                print(matrix.numbers[i].value)
                i = i + column
            elif(type(matrix.numbers[i]) == Complex):
                print(matrix.numbers[i].real, "+", matrix.numbers[i].imaginary, sep="",end="i")
                print("")
                i = i + column
        print("")

    @staticmethod
    def is_zero_matrix(matrix):
        row = matrix.row
        column = matrix.column
        i = 0
        check = True
        while(i < column*row):
            if(type(matrix.numbers[i]) == Integer):
                if not (matrix.numbers[i].value == 0):
                    return False
            else:
                return False
            i = i + 1
        return True

    @staticmethod
    def is_unit_matrix(matrix):
        row = matrix.row
        column = matrix.column
        if(row != column):
            return False
        n = row
        new_matrix = [[0 for i in range(n)]for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = matrix.numbers[k].value
                k = k + 1
        for i in range(n):
            for j in range(n):
                if(i == j):
                    if not (new_matrix[i][j] == 1):
                        return False
                else:
                    if not (new_matrix[i][j] == 0):
                        return False
        return True

    @staticmethod
    def is_top_triangular_matrix(matrix):
        row = matrix.row
        column = matrix.column
        if (row != column):
            return False
        n = row
        new_matrix = [[0 for i in range(n)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = matrix.numbers[k].value
                k = k + 1
        j = column - 1
        i = 0
        col = 0
        while (i < row - 1):
            while(j > col):
                if not(new_matrix[i][j] == 0):
                    return False
                j = j - 1
            i = i + 1
            j =  column - 1
            col = col + 1
        return True

    @staticmethod
    def is_bottom_triangular_matrix(matrix):
        row = matrix.row
        column = matrix.column
        if (row != column):
            return False
        n = row
        new_matrix = [[0 for i in range(n)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = matrix.numbers[k].value
                k = k + 1
        i = column - 1
        j = 0
        col = column - 1
        while (i > 0):
            while (j < col):
                if not (new_matrix[i][j] == 0):
                    return False
                j = j + 1
            i = i - 1
            j = 0
            col = col - 1
        return True

        @classmethod
        def make_matrix_from_string(cls, elements):
            number = elements.split(",")
            nums = []
            row = len(number)
            column = 0
            for i in range(len(number)):
                a = number[i].split()
                column = len(a)
                for j in range(len(a)):
                    a[j].strip()
                    nums.append(a[j])
            for i in range(row * column):
                if ("i" in nums[i]):
                    a = nums[i]
                    num = a.split()
                    real = int(num[0])
                    b = num[2].split('i')
                    imaginary = int(num[2][0])
                    cls.append(Complex(real, imaginary))
                else:
                    a = nums[i]
                    cls.append(Integer(a))
        return cls




list = [1, 7, 5, 2, 5, '5 + 6i', 1, 3, 45, '1 + 3i', '7 + 8i', 6]
object = Matrix(4, 3, list)
list1 = [1, 1, 1, 1, 0, 1, 1, 1 ,0, 0, 1, 1, 0, 0, 0, 0]
object1 = Matrix(4, 4, list1)
list2 = [1, 2, 3, 8]
list3 = [4, 5, 8, 3]
object2 = Matrix(2, 2, list2)
object3 = Matrix(2, 2, list3)

#Matrix.make_unit_matrix(3)     #Tested
#Matrix.get_ith_row(object, 2)  #Tested
#Matrix.get_ith_col(object, 0)
#Matrix.is_zero_matrix(object1)
#Matrix.is_unit_matrix(object)
#Matrix.is_bottom_triangular_matrix(object1)
a = Integer(5) - Integer(6)
b = Integer(6) - Complex(1, 6)
c = object + Integer(4)

