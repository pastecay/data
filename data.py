class AirCastle:
    def __init__(self, height, cloud_count, color):
        self.height = height
        self.cloud_count = cloud_count
        self.color = color

    def change_height(self, value):
        if value > 0 or (value < 0 and self.height + value >= 0):
            self.height += value

    def __add__(self, n):
        self.cloud_count += n
        self.height += n // 5
        return self

    def __call__(self, transparency):
        return self.height // transparency * self.cloud_count

    def __str__(self):
       return f"AirCastle на высоте {self.height} метров - это {self.color} с облаками {self.cloud_count}"
    def __lt__(self, other):
        if self.cloud_count != other.cloud_count:
            return self.cloud_count < other.cloud_count
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.color < other.color

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.cloud_count == other.cloud_count and self.height == other.height and self.color == other.color

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

ac1 = AirCastle(80, 3, "Hazrul")
ac2 = AirCastle(80, 1, "Dalziel")

print(ac1 < ac2)  
ac2.change_height(2)
print(ac1 > ac2)  
print(ac1, ac2, sep='\n')

class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = max(0, goodness)  

    def change_goodness(self, value):
        self.goodness = max(0, self.goodness + value)

    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.goodness)

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __lt__(self, other):
        if self.goodness != other.goodness:
            return self.goodness < other.goodness
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.name < other.name

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return self.goodness == other.goodness and self.height == other.height and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

gi1 = GoodIfrit(10, "Ifrit1", 5)
gi2 = GoodIfrit(8, "Ifrit2", 7)

gi1.change_goodness(2)
print(gi1)  # Вывод: Good Ifrit Ifrit1, height 10, goodness 7

gi3 = gi1 + 3
print(gi3)  # Вывод: Good Ifrit Ifrit1, height 13, goodness 7

result = gi1(15)
print(result) 

class Wizard:
    def __init__(self, name, rating, age_looks):
        self.name = name
        self.rating = rating
        self.age_looks = age_looks

    def change_rating(self, value):
        if 1 <= self.rating + value <= 100:
            self.rating += value
            age_change = abs(value) // 10
            if value > 0:
                self.age_looks = max(18, self.age_looks - age_change)
            else:
                self.age_looks += age_change

    def __iadd__(self, string):
        length = len(string)
        self.rating += length
        self.age_looks = max(18, self.age_looks - length // 10)
        return self

    def __call__(self, argument):
        return (argument - self.age_looks) * self.rating

    def __str__(self):
     return f"Мастер {self.name} с рейтингом {self.rating} выглядит {self.age_looks} лет"
    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age_looks != other.age_looks:
            return self.age_looks < other.age_looks
        else:
            return self.name < other.name

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.rating == other.rating and self.age_looks == other.age_looks and self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

w1 = Wizard("Merlin", 90, 25)
w2 = Wizard("Gandalf", 85, 30)

w1.change_rating(15)
print(w1) 
w1 += "Powerful"
print(w1)  

result = w1(30)
print(result) 

print(w1 < w2) 
print(w1 > w2)  
