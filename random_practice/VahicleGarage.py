
class Person:
    amount_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.amount_of_people += 1

    def introduction(self):
        print(f"Hello! my name is {self.name} and i am {self.age} years old")


class Student(Person):
    school = "RIS"

    def study_project(self,subject):
        print(f"{self.name} is currently in the making of a project on {subject}")

    def introduction(self):
        print(f"Hello! my name is {self.name}, {self.age} years old and i am a Student at {self.school}")

class Teacher(Person):
    Teacher_Salary = 3000

    def teach(self,subject):
        print(f"{self.name} is teaching {subject}")

    def raise_salary(self, amount):
        self.Teacher_Salary += amount

    def introduction(self):
        print(f"Hello! my name is {self.name}, {self.age} years old and i earn {self.Teacher_Salary} a month working at {Student.school}")


class teaching_assistant(Student, Teacher):

    def assist_student(self):
        print(f"{self.name} is a assisting {Person.amount_of_people} which is the entire school")

# ---------------- TESTS ----------------
robert = Student("Robert", 17)
camilla = Teacher("Camilla", 40)
david = Teacher("David", 35)
sam = teaching_assistant("Sam", 22)

print("--- Student ---")
robert.introduction()
robert.study_project("robotics")

print("\n--- Teacher ---")
camilla.introduction()
camilla.teach("maths")

print("\n--- Teaching assistant (inherits from both) ---")
sam.introduction()
sam.study_project("biology")
sam.raise_salary(200)
sam.assist_student()
sam.teach("physics")

print("\n--- Class variable: total people ---")
print("People created:", Person.amount_of_people)

print("\n--- Raise only affects one teacher ---")
camilla.raise_salary(1000)
print("Teacher.Teacher_Salary (class):", Teacher.Teacher_Salary)
print("camilla.Teacher_Salary:", camilla.Teacher_Salary)
print("david.Teacher_Salary:", david.Teacher_Salary)

print("\n--- Method resolution order of teaching_assistant ---")
for cls in teaching_assistant.__mro__:
    print(cls.__name__)
