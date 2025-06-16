from iii_inheritance.Employee import Employee

class Manager(Employee):
    # constructor
    def __init__(self, first_name: str, last_name: str, pay: float, employees: list[Employee] = None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        # employees = [] if employees is None else employees # ternary operator

    def add_employee(self, employee: Employee) -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self) -> None:
        for employee in self.employees:
            print(f'--> {employee.fullname()}')