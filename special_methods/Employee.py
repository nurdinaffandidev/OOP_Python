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

    ### __ : double under ie. dunder
    # if repr method not defined, fallback to default
    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.pay})"

    # if str method not defined, fallback to repr
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def __add__(self, other) -> float:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname())

# ========================================================
# create instance
emp_1 = Employee('John', 'Doe', 100)
emp_2 = Employee('Jane', 'Doff', 200)

print(emp_1)

print()
print(repr(emp_1))
print(str(emp_1))

print()
print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2) # __add__
print(len(emp_2)) # __len__

# ========================================================
print()
print(1 + 2)
print('a' + 'b')

print()
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print()
print(len('test'))
print('test'.__len__())
