
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
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    def apply_raise_class_ref(self):
        self.pay = self.pay * Employee.raise_amount


# ========================================================
# create instance
emp_1 = Employee('John', 'Doe', 100)
print(f"Number of employees = {Employee.num_of_employees}")
emp_2 = Employee('Jane', 'Doff', 200)
print(f"Number of employees = {Employee.num_of_employees}")

print(f"Employee 1: {emp_1.__dict__}")
print(f"Employee 2: {emp_2.__dict__}")

# instance methods call
print(f"\nEmployee 1 full name: {emp_1.fullname()}")
print(f"Employee 2 full name: {emp_2.fullname()}")

# class name method call, need manually pass in instance argument
print(f"\nEmployee 1 full name: {Employee.fullname(emp_1)}")
print(f"Employee 2 full name: {Employee.fullname(emp_2)}")

print(f"\nEmployee 1 pay = {emp_1.pay}")
emp_1.apply_raise()
print(f"Employee 1 pay = {emp_1.pay}")

# accessing class variables
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")

# changing class variable via class, changes reflected in all instance
Employee.raise_amount = 1.05
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")

# changing class variable via instance, changes reflected in that instance
# attribute created for that instance when assignment is done
Employee.raise_amount = 1.04  # reset back to original
emp_1.raise_amount = 1.05
print(f"\nEmployee class raise_amount = {Employee.raise_amount}")
print(f"Employee 1 raise_amount = {emp_1.raise_amount}")
print(f"Employee 2 raise_amount = {emp_2.raise_amount}")
print(emp_1.__dict__)
print(emp_2.__dict__)

# proof: no change
emp_1.pay = 100 # reset back to original
Employee.raise_amount = 1.04 # reset back to original
print(f"Employee 1 pay = {emp_1.pay}")
emp_1.apply_raise() # referencing self
print(f"Employee 1 pay = {emp_1.pay}")

emp_1.pay = 100 # reset back to original
print(f"Employee 1 pay = {emp_1.pay}")
emp_1.apply_raise_class_ref() # referencing class
print(f"Employee 1 pay = {emp_1.pay}")