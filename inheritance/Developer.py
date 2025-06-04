from inheritance.Employee import Employee

class Developer(Employee):
    raise_amount = 1.10 # this overrides parent raise_amount

    # constructor
    def __init__(self, first_name: str, last_name: str, pay: float, prog_language: str):
        super().__init__(first_name, last_name, pay)
        # Employee.__init__(self, first_name, last_name, pay) # same as calling super()
        self.prog_language = prog_language
