
class FruitType:
    def __init__(self, Vname, Vprotein, Vcarbs, Vfat):
        fruits = ['apple', 'orange', 'lemon', 'banana', 'cucumber', 'peach']
        if (Vname in fruits):
            self.Vname = Vname
        else:
            raise ValueError('This fruit does not allow')
        self.Vprotein = Vprotein
        self.Vcarbs = Vcarbs
        self.Vfat = Vfat

    @property
    def Vprotein(self):
        return self._Vprotein

    @Vprotein.setter
    def Vprotein(self, Vprotein):
        if not(Vprotein > 5):
            raise ValueError('This fruit does not allow')
        self._Vprotein = Vprotein

    @property
    def Vcarbs(self):
        return self._Vcarbs

    @Vcarbs.setter
    def Vcarbs(self, Vcarbs):
        if not (Vcarbs > 80):
            raise ValueError('This fruit does not allow')
        self._Vcarbs = Vcarbs

    @property
    def Vfat(self):
        return self._Vfat

    @Vfat.setter
    def Vfat(self, Vfat):
        if not (Vfat < 2):
            raise ValueError('This fruit does not allow')
        self._Vfat = Vfat

    def Name(self):
        return self.Vname

    def Protein(self):
        return self._Vprotein

    def Carbs(self):
        return self._Vcarbs

    def Fat(self):
        return self._Vfat



class Fruit():
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

    def Type(self):
        return self.type

    def Weight(self):
        return self.weight

    def Protein(self):
        if (self.type.Protein() == None):
            raise ValueError('Error')
        a = self.type.Protein()
        return a

    def Carbs(self):
        if (self.type.Carbs() == None):
            raise ValueError('Error')
        a = self.type.Carbs()
        return a

    def Fat(self):
        if (self.type.Fat() == None):
            raise ValueError('Error')
        a = self.type.Fat()
        return a

    def __str__(self):
        return self.type.Vname + " " + str(self.type.Protein()) + " " + str(self.type.Carbs()) + " " +\
               str(self.type.Fat())



class Cempare:
    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def compare(self):
        p1 = self.fruit1.Protein()
        p2 = self.fruit2.Protein()
        c1 = self.fruit1.Carbs()
        c2 = self.fruit2.Carbs()
        f1 = self.fruit1.Fat()
        f2 = self.fruit2.Fat()
        count1 = 0
        count2 = 0
        if(p1 >= p2):
            count1 = count1 + 1
        else:
            count2 = count2 + 1
        if (c1 >= c2):
            count1 = count1 + 1
        else:
            count2 = count2 + 1
        if (f1 <= f2):
            count1 = count1 + 1
        else:
            count2 = count2 + 1
        if(count1 > count2):
            print("fruit1")
        else:
            print("fruit2")


fruittype1 = FruitType("banana", 6.5, 93, 0.5)
fruittype2 = FruitType("orange", 9, 90, 1)
fruit1 = Fruit(fruittype1, 110)
fruit2 = Fruit(fruittype2, 100)
com = Cempare(fruit1, fruit2)
com.compare()

