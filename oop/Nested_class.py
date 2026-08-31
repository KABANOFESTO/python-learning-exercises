class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_info(self):
            return f"{self.name} - {self.position}"

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee_name, employee_position):
        employee = self.Employee(employee_name, employee_position)
        self.employees.append(employee)

    def list_employees(self):
        return [employee.get_info() for employee in self.employees]


company = Company("TechCorp")
company.add_employee("Alice", "Software Engineer")
company.add_employee("Bob", "Data Scientist")
company.add_employee("Charlie", "Product Manager")

print("Employees:")
for employee in company.list_employees():
    print(employee)
