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




class Dog:
     def __init__(self, name: str, breed: str, age: int) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        
    # Methods
     def bark(self):
        return f"{self.name} is barking"

     
# Creating a new object
my_dog = Dog("Buddy", "Golden Retriever", 3)

print(my_dog.bark())


class Cat:
    def __init__(self, name: str) -> None:
        self.name =  name

    # Methods
    def sound(self):
      return f"{self.name} is meowing"
    
    def get_name(self):
        return f"The name of my cat is {self.name}"
    
# Creating a new object
my_cat = Cat("Milo")

print(my_cat.sound())

# create a new object
my_cat2 = Cat("Jimmy")
print(my_cat2.sound())

print(my_cat.get_name())
print("-----THIS IS THE SECOND OBJECT-----")
print(my_cat2.get_name())

print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("MORE EXAMPLES")

class Student:
    def __init__(self, name: str, age: int, grade: str) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
   
# Creating a new object
class Course:
    def __init__(self, name: str, max_students: int) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []

        # Methods

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_student_name(self):
        return self.name
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    
    def get_highest_score(self):
        value = 0
        for student in self.students:
            if student.get_grade() > value:
                value = student.get_grade()
        return value


    def get_highest_score_student(self):
        
        highest_grade = 0
        for student in self.students:
            if student.get_grade() > highest_grade:
                highest_grade = student.get_grade()
                highest_student = student
        return highest_student
# creatig instances

s1 = Student("Billy", 20, 85)
s2 = Student("Johnny", 20, 67)
s3 = Student("Dimmy", 20, 45) 

# creating a course
course = Course("Science", 2)
# adding students to the course
course.add_student(s1)
course.add_student(s2) 

highest_student = course.get_highest_score_student()
print("Average: ", course.get_average_grade())
print("The student with the highest score is: ", highest_student.get_name(), "With a score of", course.get_highest_score())

