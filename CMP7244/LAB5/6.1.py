class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def get_name(self, name):
        self.name = name

    def get_address(self, address):
        self.address = address

    def get_age(self, age):
        self.age = age

    def __str__(self):
        return 'Name: %s , Address: %s , Age: %d' % (self.name, self.address, self.age)


class Employee(Person):
    def __init__(self, name, address, age):
        Person.__init__(self, name, address, age)


def main():
    E1 = Employee('Raju', 'India', 40)
    E2 = Employee('Ronak', 'US', 25)
    print(E1.name)
    print(E2.age)


main()
