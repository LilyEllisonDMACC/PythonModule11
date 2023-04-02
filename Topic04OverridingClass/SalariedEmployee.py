"""
Program: SalariedEmployee.py
Author: Lily Ellison
Last date modified: 04/02/2023

The purpose of this program is to create a subclass, SalariedEmployee, which inherits attributes and override methods
from the Employee class.

"""
#import from base class:
from Topic04OverridingClass.Employee import Employee as Emp


class SalariedEmployee(Emp):

    def __init__(self, lname, fname, sd, sal):
        #create salaried employee with constructor that calls base class constructor
        super().__init__(lname, fname)
        self._start_date = sd
        #format salary to include commas every 3 digits
        self._salary = "{:,}".format(sal)

    def give_raise(self, new_sal):
        #update with new, formatted salary
        self._salary = "{:,}".format(new_sal)

    def display(self):
        #override base class display method
        return Emp.display(self) + "\nStart Date: " + str(self._start_date) + "\nSalary: $" + str(self._salary) + ' per year\n'



if __name__ == '__main__':
    #create and display salaried employee:
    SalEmp = SalariedEmployee("Ellison", "Lily", "4/2/23", 40000)
    print(SalEmp.display())
    #update salary and display again:
    SalEmp.give_raise(45000)
    print(SalEmp.display())

    #delete member:
    del SalEmp


"""
Testing/Results:

Ellison, Lily
Start Date: 4/2/23
Salary: $40,000 per year.

Ellison, Lily
Start Date: 4/2/23
Salary: $45,000 per year.


Process finished with exit code 0

"""