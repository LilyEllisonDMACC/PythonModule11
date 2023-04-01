"""
Program: Person.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to create a person class that uses both the student and address classes and display the information.

"""
from PersonStudent.Address import Address
from PersonStudent.Student import Student


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy, stu):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.student_info = stu

    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + '\n' + str(self.address.display()) + '\n' + str(self.student_info.display())


#Driver
if __name__ == "__main__":
    good_student = Student("CIS", "Jan 2022", 4.0)
    my_address = Address("3100", "Diamond", "Street", "Ames", "IA", '50010')
    awesome_person = Person("Ellison", "Lily", my_address, good_student)
    print(awesome_person.display())
    good_student.change_major("Being Awesome!")
    good_student.update_gpa(3.0)
    print(awesome_person.display())

