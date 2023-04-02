"""
Program: HourlyEmployee.py
Author: Lily Ellison
Last date modified: 04/02/2023

The purpose of this program is to create a subclass, HourlyEmployee, which inherits attributes and override methods
from the Employee class.

"""
# imports base class
from Topic04OverridingClass.Employee import Employee as Emp


class HourlyEmployee(Emp):
    def __init__(self, lname, fname, sd, sal: float):
        #uses base class to construct HourlyEmployee with salary as a float so decimals can be added
        super().__init__(lname, fname)
        self._start_date = sd
        # formats salary to include 2 decimal points
        self._salary = "{:.2f}".format(sal)

    def give_raise(self, new_sal):
        # updates formatted salary
        self._salary = "{:.2f}".format(new_sal)

    def display(self):
        return Emp.display(self) + "\nStart Date: " + str(self._start_date) + "\nSalary: $" + str(self._salary) + ' per hour.\n'
        #display method that overrides base class


if __name__ == '__main__':
    #create hourly employee and display:
    HourEmp = HourlyEmployee("Ellison", "Lily", "4/2/23", 10)
    print(HourEmp.display())
    #update pay and display:
    HourEmp.give_raise(12)
    print(HourEmp.display())


"""
Testing/Results:

Ellison, Lily
Start Date: 4/2/23
Salary: $10.00 per hour.

Ellison, Lily
Start Date: 4/2/23
Salary: $12.00 per hour.


Process finished with exit code 0

"""