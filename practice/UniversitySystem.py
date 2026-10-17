from abc import ABC , abstractmethod


class Department:

    def __init__(self,name):
        self.name = name
        self.student_number = []
        self.professor_number = []

    def add_student(self, student):
        if student in self.student_number:
            return f"{student} is already enrolled in {self.name} Department"
        elif student not in self.student_number:
            self.student_number.append(student)
            return f"{student} has been successfully added to {self.name}"
        else:
            return f"You have not entered the name of the student you want to add"


    def add_professor(self,professor):
        if professor in self.professor_number:
                return f"{professor} is already present in the {self.name} Department"
        elif professor not in self.professor_number:
            self.professor_number.append(professor)
            return f"{professor} has been successfully added to {self.name}"
        else:
            return f"You have not entered the name of the professor you want to add"

    def show_everyone_in_department(self):
        print("Student's: ")
        for i , student in enumerate(self.student_number):
            print(f"{student} , {i}")
        print("Professor's: ")
        for q , professor in enumerate(self.professor_number):
            print(f"{professor} , {q}")

class University:

    def __init__(self,name,date_of_foundation):
        self.name = name
        self.date_of_foundation = date_of_foundation
        self.departments = []


    def close_department(self,name):
        if self.get_department(name) is None:
            return f"{name} Cannot be removed because it is not available in the current list of departments in {self.name} University"
        else:
            self.departments.remove(self.get_department(name))
            return f"Successfully Removed {name} from {self.name} University"


    def open_department(self, department):
        if self.get_department(department) is not None:
            name = department.name if isinstance(department, Department) else department
            return f"The {name} is already available in the current list of departments in {self.name} University so it cannot be added"
        else:
            self.department = Department(department)
            self.departments.append(self.department)
            return f"The {department} has been officially added to the list of available departments in {self.name} University"

    def Summary(self):
        if not self.departments:
            print(f"There are no departments available in {self.name} University")
        for i , department in enumerate(self.departments):
            print(f"Department Number : {i} ,Date Of Foundation : {self.date_of_foundation}, Department Name : {department.name},Number Of Student's : {len(department.student_number)},Number Of Professor's : {len(department.professor_number)}")

    def get_department(self,name):
        for department in self.departments:
            if name == department.name:
                return department
            else:
                continue


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


oxford = University(name="Oxford", date_of_foundation=1096)
oxford.Summary()
print(oxford.open_department("Computer Science"))
print(oxford.open_department("Mathematics"))
print(oxford.open_department("Computer Science"))
cs = oxford.get_department("Computer Science")
maths = oxford.get_department("Mathematics")
print(cs.name)
print(oxford.get_department("Physics"))
prof = Professor(name="Alan Turing", subject="Computer Science", university=oxford.name)
student = Students(name="Ada Lovelace", year=2, university=oxford.name)
print(prof.describe())
print(student.describe())
try:
    People_In_school("Nobody")
except TypeError as e:
    print(f"TypeError: {e}")
print(cs.add_student(student.name))
print(cs.add_student(student.name))
print(cs.add_student("Grace Hopper"))
print(cs.add_student(""))
print(maths.add_student("Isaac Newton"))
print(cs.add_professor(prof.name))
print(cs.add_professor(prof.name))
print(cs.add_professor(""))
cs.show_everyone_in_department()
oxford.Summary()
print(oxford.close_department("Physics"))
print(oxford.close_department("Mathematics"))
print(oxford.close_department("Mathematics"))
oxford.Summary()
