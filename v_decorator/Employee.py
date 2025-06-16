class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name + "." + last_name + "@company.com" # commented out to allow email computed dynamically via first_name, last_name

    @property # @property turns a method into a read-only attribute.
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self) -> str:
        if self.first_name is None or self.last_name is None:
            return "no registered email"
        return f"{self.first_name}.{self.last_name}@company.com"

    @fullname.setter
    def fullname(self, fullname: str):
        first_name, last_name = fullname.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print(f"Deleting name for employee: {self.fullname}")
        self.first_name = None
        self.last_name = None

# ========================================================
# create instance
emp_1 = Employee('John', 'Doe', 100)
emp_2 = Employee('Jane', 'Doff', 200)

emp_1.first_name = "Sam"
print(emp_1.first_name)
print(emp_1.fullname)
print(emp_1.email)
print()

emp_1.fullname = "Jackson Wang" # w/o setter this will result in AttributeError: property 'fullname' of 'Employee' object has no setter

print(emp_1.fullname)
print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.email)
print()

del emp_1.fullname
print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.email)



