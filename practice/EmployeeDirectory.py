

class Employee:
    employee_number = 0
    company_wide_raise_percentage = 4
    all_employee = []

    def __init__(self, name, job_title, yearly_salary) -> None:
        if Employee.check(yearly_salary):
            self.yearly_salary = yearly_salary
        else:
            raise ValueError("Salary mus be more than 0")
        self.name = name
        self.job_title = job_title
        Employee.employee_number += 1
        Employee.all_employee.append(self)

    @classmethod
    def find_employee(cls,employee_name):
        for employee in cls.all_employee:
            if employee_name == employee.name:
                employee.display_employee()
                break
        else:
            return f"The employee name does not seem to be available in our employee list"

    def display_employee(self):
        print(f"{self.name} - {self.job_title} - {self.yearly_salary:,.2f} €")

    def raise_salary(self):
        if Employee.check(self.yearly_salary):
            self.yearly_salary = self.yearly_salary + ((self.yearly_salary) / 100) * (Employee.company_wide_raise_percentage)
            return f"Successfully raised salary to {self.yearly_salary} Euros"
        else:
            return f"Your salary is currently negative please contact your admin for support"


    @classmethod
    def from_dict_create_employee(cls,dictionary):
        if not isinstance(dictionary,dict):
            return "The value u entered is not a dictionary"
        else:
            values = []
            for i in dictionary:
                values.append(i)
            if "name" in values:
                if "job_title" in values:
                    if "salary" in values:
                        if cls.check(dictionary["salary"]):
                            x = cls(dictionary["name"],dictionary["job_title"],dictionary["salary"])
                            print(f"Successfully created an employee account for {x.name}")
                            return x
                        else:
                            print(f"Your salary is currently negative please contact your admin for support")
                    else:
                        print(f"Your dictionary does not contain a salary key")
                else:
                    print(f"Your dictionary does not contain a job_title key")
            else:
                print(f"Your dictionary does not contain a name key")



    @classmethod
    def from_sentence_create_employee(cls,sentence):
        try:
            name , title , salary = sentence.split(",")
            salary = float(salary)
            if isinstance(name, str):
                if isinstance(title, str):
                    if isinstance(salary, float) and cls.check(salary):
                        x = cls(name,title,salary)
                        print(f"Successfully created an employee account for {x.name}")
                        return x
                    else:
                        print(f"Your Salary needs to only contain number's")
                else:
                    print(f"Your title is required to only contain letter's")
            else:
                print(f"Your Username or name is required to only contain letter's")
        except(ValueError):
            return f"You Have Entered an incorrect sentence format"


    @staticmethod
    def check(salary):
        if salary <= 0:
            return False
        else:
            return True





anna = Employee.from_sentence_create_employee("Anna,Engineer,52000")
anna.display_employee()
luca = Employee("Luca", "Developer", 30000)
luca.display_employee()
print(luca.raise_salary())
marco = Employee.from_dict_create_employee({"name": "Marco", "job_title": "Designer", "salary": 40000})
Employee.from_dict_create_employee({"name": "Giulia", "salary": 45000})
print(Employee.from_dict_create_employee("not a dict"))
print(Employee.from_sentence_create_employee("Bob Manager 60000"))
Employee.from_sentence_create_employee("Bob,Manager,-5")
try:
    Employee("Zero", "Intern", 0)
except ValueError as e:
    print(f"ValueError: {e}")
Employee.find_employee("Marco")
print(Employee.find_employee("Nobody"))
print("Employees created:", Employee.employee_number)
