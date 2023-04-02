"""
Program: Manager.py
Author: Lily Ellison
Last date modified: 04/02/2023

The purpose of this program is to create a class, manager, that inherits from both employee and person classes.

"""
#I used SalariedEmployee instead of the Employee class as it contained the information requested
from Topic04OverridingClass.SalariedEmployee import SalariedEmployee as SalEmp
from DerivedPersonStudent.Person import Person as P


class Manager(P, SalEmp):
    def __init__(self, lname, fname, sd, sal, dep):
        #create manager with constructor that calls base classes constructors
        #constructor for Person:
        super().__init__(lname, fname)
        #uses constructor for class listed after Person class, but before self class
        super(P, self).__init__(lname, fname, sd, sal)
        #sets department, as it is not in either base class
        self._department = dep

    def display(self):
        #override base class display method
        return SalEmp.display(self) + "Department: " + str(self._department)


if __name__ == '__main__':
    #creates and displays a manager class instance:
    Mom = Manager("Ellison", "Lily", "4/2/22", 40000, "House")
    print(Mom.display())
    #create employees:
    husband = SalEmp("Ellison", "Mackenzie", "4/2/23", 40000)
    daughter1 = SalEmp("Ellison", "Roseanna", "4/2/23", 40000)
    daughter2 = SalEmp("Ellison", "Maybelle", "4/2/23", 40000)
    #add employees to list:
    direct_reports = [husband, daughter2, daughter1]
    #print title of list:
    print("\nDirect Reports:\n")
    #print list:
    for member in direct_reports:
        print(SalEmp.display(member))

    #delete members:
    del Mom
    del husband
    del daughter2
    del daughter1


"""
Testing/Running:
Ellison, Lily
Start Date: 4/2/22
Salary: $40,000 per year
Department: House

Direct Reports:

Ellison, Mackenzie
Start Date: 4/2/23
Salary: $40,000 per year

Ellison, Maybelle
Start Date: 4/2/23
Salary: $40,000 per year

Ellison, Roseanna
Start Date: 4/2/23
Salary: $40,000 per year


Process finished with exit code 0

"""
