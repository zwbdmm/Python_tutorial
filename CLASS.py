#I will make this change to test the git function
#Objective class
##ahout the class:
class Employee:
    number_of_emps = 0

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        Employee.number_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee('Michael', 'Jackson',50000)
emp_2 = Employee('Larry', 'Peter',60000)

print(emp_1 + emp_2)

print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())
print(str(emp_1))
print(emp_1.__str__())

#print(emp_1.fullname())
#print(Employee.fullname(emp_2))

emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

#use __dict__ to see the all the stuff inside.
print(emp_1.__dict__)
print(Employee.__dict__)

#reset the parameter for raise amount for a class
print(emp_1.raise_amount)
print(Employee.raise_amount)

#reset the parameter for raise amount for a instance
emp_1.raise_amount = 1.5
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_1.__dict__)

print(Employee.number_of_emps)

#about the class method
Employee.set_raise_amount(3)
print(emp_2.raise_amount)
print(emp_1.raise_amount)

emp_str_1 = 'Cece-Furtner-10000'
emp_str_2 = 'Frank-Liu-10000'
emp_str_3 = 'Bangde-Liu-20000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.fullname())

#about the staticmethod
import datetime
my_date = datetime.date(2017,10,22)
print(Employee.is_workday(my_date))

##############################################################################
##########################      Inheritence          ##########################
##############################################################################
class Developer(Employee):
    raise_amount =1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Jack', 'Ma', 20000, 'Python')
dev_2 = Developer('Jeff', 'Wu', 30000, 'C++')

print(dev_2.prog_lang)


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr_1 = Manager('Wenbin','Zhu', '90000', employees = [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) #True
print(isinstance(mgr_1, Employee)) #True
print(isinstance(mgr_1, Developer)) #False

print(issubclass(Manager, Developer)) #FALSE
print(issubclass(Manager, Employee)) #TRUE

####################################################################################














