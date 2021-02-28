class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps +=1

        @property
        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        print('Delete Name')
        self.first = None
        self.last = None

        @fullname.deleter
        def fullname(self):
            first, last = name.split(' ')
            self.first = first
            self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email )

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


emp_1 = Employee('Rafa', 'Raja', 30000)
emp_2 = Employee('Nida', ' Raja', 333000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(emp_1.fullname())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
