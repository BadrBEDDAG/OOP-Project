class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name_and_age(self):
        return self.name +" is " + str(self.age) + " years old !"

    def add_one(self, x):
        return x + 1
        
    def bark(self):
        print("bark")

    def set_age(self, age):
        self.age = age

d = Dog("Tim",25)     # d est un objet de type Dog()
d.set_age(26)
print(d.get_name_and_age())


###################################                     A more complicated example                   #######################


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

Student_1 = Student("Tim", 25, 100)
Student_2 = Student("Bill", 26, 99)
Student_3 = Student("Jill", 24, 98)

course_1 = Course("Python", 2)
course_1.add_student(Student_1)
course_1.add_student(Student_2)


print(course_1.get_average_grade())

##############################################                INHERITANCE                 ####################################33

class Pet:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color: str):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 25)
p.show()

c= Cat("Bill",25,"Red")
c.show()


# What we did in the example avove is better than this below

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark")


######################################### Attributes specific to a class and not tgo an instance ##################################


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim")
print(p1.number_of_people)

p2 = Person("Jill")

Person.number_of_people = 10

print(p2.number_of_people)


######################################## Class methods ########################################
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    @classmethod
    def number_of_people(cls)
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @staticmethod

p1 = Person("Tim")
print(p1.number_of_people)

p2 = Person("Jill")

Person.number_of_people = 10

print(p2.number_of_people)