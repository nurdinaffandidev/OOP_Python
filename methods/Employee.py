import datetime

class Employee:

    # class variables (shared among all instances)
    raise_amount = 1.04
    num_of_employees = 0

    # constructor
    # - attributes (ie. instance variables) are within constructor
    # - instance variables are unique to each instance
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"
        Employee.num_of_employees += 1 #

    # regular methods in a class take instance as first argument
    # def fullname(self):
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    # def apply_raise_class_ref(self):
    def apply_raise_class_ref(self) -> None:
        self.pay = self.pay * Employee.raise_amount

    # class methods, takes class as first argument
    @classmethod
    # def set_raise_amount(cls, int):
    def set_raise_amount(cls, amount: int) -> None:
        cls.raise_amount = amount

    # class methods as alternative constructors
    @classmethod
    # def from_string(cls, emp_str):
    def from_string(cls, emp_str: str) -> "Employee":
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

    # static method does not take class/instance as first argument
    # - use static method if method does not access instance/class within the function
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# ========================================================
# create instance
emp_1 = Employee('John', 'Doe', 100)
emp_2 = Employee('Jane', 'Doff', 200)

# print original raise_amount value
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")

# calling class method doesn't require to pass any instance as first arg is the class itself
Employee.set_raise_amount(1.05)
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")

# instance can call class method but doesn't really make sense though
# not done in normal practice
emp_1.set_raise_amount(1.06)
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")

# manual string parsing to create instance
emp_str_3 = 'Sam-Smith-80000'
first_name, last_name, pay = emp_str_3.split('-')
emp_3 = Employee(first_name, last_name, pay)
print(f"\nemp_3 = {emp_3.__dict__}")

# using class method as alternative constructor
emp_str_4 = 'Joe-Brov-90000'
emp_4 = Employee.from_string(emp_str_4)
print(f"\nemp_4 = {emp_4.__dict__}")

today = datetime.date.today()
my_date = datetime.date(2016, 7, 10)
print(f"\n{Employee.is_workday(today)}")
print(f"{Employee.is_workday(my_date)}")
