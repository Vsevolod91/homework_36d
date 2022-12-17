class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        return f"{self.name} {self.stud_id} \n{self.lap.brand} {self.lap.cpu} {self.lap.ram}"

    class Laptop:
        def __init__(self, brand="HP", cpu="i5", ram="8gb"):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)

print(s1.show())

s1.lap.ram = 16
s1.lap.brand = "Lenovo"
print(s1.show())

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))