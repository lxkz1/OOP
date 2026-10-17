class Company:
    class Employee:
        def __init__(self,name,position) -> None:
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} , {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employee.append(new_employee)

    def list_employees(self):
        return [employee.get_details()for employee in self.employee]


company = Company("Krusty Krab")
company2 = Company("Chum Bucket")

companies = [company,company2]

company.add_employee("Eugene", "Manager")
company.add_employee("Spoongebob", "Cook")
company.add_employee("SquidWard", "Cashier")


company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Asistant")
company2.add_employee("Dave", "Engineer")

for company in companies:
    for employee in company.employee:
        print(employee.get_details())
