class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def __add__(self,other):
        return self.age + other.age

rahim = Person('Rahim',26)
madi = Person('Madeeha',16)

print(rahim + madi)