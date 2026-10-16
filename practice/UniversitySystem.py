from abc import ABC , abstractmethod


class Department:

    def __init__(self,name):
        self.name = name
        self.student_number = []
        self.professor_number = []

    def add_student_or_professor(self, student="",professor=""):
        if student != "":
            if student in self.student_number:
                return f"{student} is already enrolled in {self.name} Department"
            else:
                self.student_number.append(student)
                return f"{student} has been successfully added to {self.name}"
        elif professor != "":
            if professor in self.professor_number:
                return f"{professor} is already present in the {self.name} Department"
            else:
                self.professor_number.append(professor)
                return f"{professor} has been successfully added to {self.name}"
        else:
            return f"You have not the name of the student"

    def show_everyone_in_department(self):
        print("Student's: ")
        for i , student in enumerate(self.student_number):
            print(f"{student} , {i}")
        print("Professor's: ")
        for q , professor in enumerate(self.professor_number):
            print(f"{professor} , {q}")

class University:

    def __init__(self,name,date_of_foundation,department):
        self.name = name
        self.date_of_foundation = date_of_foundation
        self.department = Department(department)
        self.departments = []
        self.departments.append(self.department)


    def close_department(self,department):
        if department in self.departments:
            self.departments.remove(department)
            return f"Successfully Removed {department.name} from {self.name} University"
        else:
            name = department.name if isinstance(department, Department) else department
            return f"{name} Cannot be removed because it is not available in the current list of departments in {self.name} University"

    def open_department(self, department):
        if department in self.departments:
            return f"The {department.name} is already avaiable in the current list of departments in {self.name} University so it cannot be added"
        else:
            self.departments.append(department)
            return f"The {department.name} has been officially added to the list of available departments in {self.name} University"

    def Summary(self):
        for i , department in enumerate(self.departments):
            print(f"Department Number : {i} ,Department Name : {department.name},Number Of Student's : {len(department.student_number)},Number Of Professor's : {len(department.professor_number)}")


class People_In_school(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def describe(self):
        pass


class Professor(People_In_school):
    def __init__(self, name, subject, university):
        super().__init__(name)
        self.subject = subject
        self.university = university

    def describe(self):
        return f"Hello i am {self.name} and i teach {self.subject} at {self.university}"

class Students(People_In_school):
    def __init__(self, name, year,university):
        super().__init__(name)
        self.year = year
        self.university = university

    def describe(self):
        return f"Hello i am {self.name} and i am Year {self.year} at {self.university}"

oxford = University(name="Oxford", date_of_foundation=1096, department="Computer Science")
cambridge = University(name="Cambridge", date_of_foundation=1209, department="Mathematics")
cs = oxford.department
maths = cambridge.department
prof = Professor(name="Alan Turing", subject="Computer Science", university=oxford.name)
student = Students(name="Ada Lovelace", year=2, university=oxford.name)
print(prof.describe())
print(student.describe())
print(cs.add_student_or_professor(student=student.name))
print(cs.add_student_or_professor(student=student.name))      
print(cs.add_student_or_professor(professor=prof.name))
print(cs.add_student_or_professor(professor=prof.name))       
print(cs.add_student_or_professor())                          
print(maths.add_student_or_professor(student="Isaac Newton"))
try:
    People_In_school("Nobody")
except TypeError as e:
    print(f"TypeError: {e}")
print(oxford.open_department(cs))
print(oxford.close_department("Physics"))                     
print(oxford.close_department(maths))
cs.show_everyone_in_department()
oxford.Summary()
print(oxford.close_department(cs))
oxford.Summary()                                           
