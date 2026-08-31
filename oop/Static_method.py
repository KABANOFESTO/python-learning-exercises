class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Software Engineer", "Data Scientist", "Product Manager"]
        return position in valid_positions


employee1 = Employee("Alice", "Software Engineer")
employee2 = Employee("Bob", "Intern")

print(employee1.get_info())  # Returns "Alice - Software Engineer"
print(employee2.get_info())  # Returns "Bob - Intern"

print(Employee.is_valid_position("Software Engineer"))  # Returns True
print(Employee.is_valid_position("Intern"))  # Returns False
