class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"


# ========================================================
# create instance
emp_1 = Employee('John', 'Doe', 100)
emp_2 = Employee('Jane', 'Doff', 200)

emp_1.first_name = "Sam"
print(emp_1.first_name)
print(emp_1.fullname())
print(emp_1.email) # notice email does not reflect first_name change