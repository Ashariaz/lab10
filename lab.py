class Person:
    def __init__(self,name , age ,address):
        self.__name = name
        self.__age = age
        self.__address = address

    def set_name(self, x):
        self.name = x

    def get_name(self):
        return self.name
    def set_age(self, x):
        self.age = x

    def get_age(self):
        return self.age
    def set_address(self, x):
        self.address = x

    def get_address(self):
        return self.address

a = Lab("abc",20,"xyz")
a.set_name("ashar")
a.set_age(21)
a.set_address("lahore")
print(a.get_name())
print(a.get_age())
print(a.get_address())
