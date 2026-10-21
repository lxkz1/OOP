import contextlib
import io
import unittest

with contextlib.redirect_stdout(io.StringIO()):
    from EmployeeDirectory import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        Employee.all_employee = []
        Employee.employee_number = 0
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()

    def tearDown(self):
        self.quiet.__exit__(None, None, None)

    def test_create_employee(self):
        emp = Employee("Luca", "Developer", 30000)
        self.assertEqual(Employee.employee_number, 1)
        self.assertIn(emp, Employee.all_employee)

    def test_invalid_salary_raises(self):
        with self.assertRaises(ValueError):
            Employee("Luca", "Developer", 0)

    def test_raise_salary(self):
        emp = Employee("Luca", "Developer", 1000)
        emp.raise_salary()
        self.assertEqual(emp.yearly_salary, 1040)

    def test_from_dict(self):
        emp = Employee.from_dict_create_employee({"name": "Anna", "job_title": "Engineer", "salary": 52000})
        self.assertEqual((emp.name, emp.job_title, emp.yearly_salary), ("Anna", "Engineer", 52000))
        self.assertIsNone(Employee.from_dict_create_employee({"name": "Anna", "salary": 52000}))
        self.assertIsInstance(Employee.from_dict_create_employee("not a dict"), str)

    def test_from_sentence(self):
        emp = Employee.from_sentence_create_employee("Anna,Engineer,52000")
        self.assertEqual((emp.name, emp.job_title, emp.yearly_salary), ("Anna", "Engineer", 52000.0))
        self.assertIn("incorrect", Employee.from_sentence_create_employee("Anna Engineer 52000"))
        self.assertIsNone(Employee.from_sentence_create_employee("Anna,Engineer,-5"))

    def test_find_employee(self):
        Employee("Luca", "Developer", 30000)
        self.assertIsNone(Employee.find_employee("Luca"))
        self.assertIn("not seem", Employee.find_employee("Nobody"))


if __name__ == "__main__":
    unittest.main()
