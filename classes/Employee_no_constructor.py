
class Employee_no_constructor:
    pass

# create instance
emp1_no_cons = Employee_no_constructor()
emp2_no_cons = Employee_no_constructor()

# print(emp1_no_cons)
# print(emp2_no_cons)

# assign attributes directly from instance
emp1_no_cons.first_name = 'John'
emp1_no_cons.last_name = 'Doe'
emp1_no_cons.pay = 50000

emp2_no_cons.first_name = 'Jane'
emp2_no_cons.last_name = 'Smith'
emp1_no_cons.pay = 20000

print(f"Employee 1: {emp1_no_cons.__dict__}")
print(f"Employee 2: {emp2_no_cons.__dict__}")
