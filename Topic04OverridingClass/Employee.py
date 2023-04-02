"""
Program: Employee.py
Author: Lily Ellison
Last date modified: 04/02/2023

The purpose of this program is to create a base class, Employee, which subclasses SalariedEmployee and HourlyEmployee
will use to inherit attributes and override methods.

"""

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)

# Driver
'''
emp = Employee('Ruiz', 'Matthew')   # call the construtor, needs to have a first and last name in parameter

print(emp.display())                # display returns a str, so print the information

del emp
'''