class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self):
        return self.price - 100


product1 = Product("りんご", 500)

print(product1.discount())

class Car:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
car1 = Car("GTR",300)
print(f"名前:{car1.name}")
print(f"速度:{car1.speed}")

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
Student1 = Student("佐藤",85)
print(f"名前:{Student1.name}")
print(f"点数:{Student1.score}")





