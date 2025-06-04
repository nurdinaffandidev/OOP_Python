from inheritance.Developer import Developer
from inheritance.Employee import Employee
from inheritance.Manager import Manager

# Main runner
dev_1 = Developer('John', 'Doe', 1000, 'python')
dev_2 = Developer('Same', 'Smith', 2000, 'java')

print("\nDevelopers:")
print(dev_1.__dict__)
print(dev_2.__dict__)

# print(help(Developer))

# shows child class overriding of parent class var raise_amount
print(f"\nEmployee raise_amount = {Employee.raise_amount}")
print(f"Developer raise_amount = {Developer.raise_amount}")

print("\nManagers:")
manager_1 = Manager('James', 'Gunn', 3000)
manager_2 = Manager('Jonny', 'Rich', 4000, [dev_1, dev_2])

print(manager_1.__dict__)
print(manager_2.__dict__)

print("\nManager1:")
manager_1.add_employee(manager_2)
manager_1.print_employees()

print("\nManager2:")
manager_2.remove_employee(dev_2)
manager_2.print_employees()

print()
print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))
print(isinstance(dev_1, Employee))

print()
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
