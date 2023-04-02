"""
Program: Person.py
Author: Lily Ellison
Last date modified: 04/01/2023

The purpose of this program is to create a person class that uses both the student and address classes and display the information.

"""


class Person:

    def __init__(self, lname, fname, addy=''):
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + str(self.address)
