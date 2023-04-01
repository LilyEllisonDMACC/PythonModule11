"""
Program: Student.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to create a student class used in the person class.

"""

class Student:
    def __init__(self, m, sd, gpa):
        self.major = m
        self.start_date = sd
        self.gpa = gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return "Major: " + str(self.major) + ", Started: " + str(self.start_date) + '\nGPA: ' + str(self.gpa)