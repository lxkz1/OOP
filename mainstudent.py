class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"the number of students in the class of {Student.class_year} is {Student.num_students}")
print(f"{student1.name},{student2.name},{student3.name} and {student4.name}")
