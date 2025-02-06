#OOP in python

class Car:
    # class attribute
    wheels = 4


# Constructor function

    def __init__(self, make: str, model: str, color: str, year: int) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # Methods

    def description(self):
        return f"I am driving a {self.year}, {self.make}, {self.model} automobile"
    
    def start_engine(self):
        return f"The engine is now runing on {self.wheels} wheels"
    

 # Creating a new object
 


    # Accessing attributes

my_car = Car("Toyota", "Land cruiser", "Red", 2025)
print(my_car.description())


class School:
    # class attribute
    school_name = "AkiraChix"
    # Constructor function
    def __init__(self, name: str, room: int, teachers: str) -> None:
        self.name = name
        self.room = room
        self.teachers = teachers

        # Methods
    def identity(self):
            return f"The name of my school is {self.name} and I am in room {self.room}"# Creating a new object
     

    # Creating a new object
my_school = School("AkiraChix", 10, "Mr. John")
    # Accessing attributes
print(my_school.identity())

