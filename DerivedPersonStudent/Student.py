"""
Program: Student.py
Author: Lily Ellison
Last date modified: 04/01/2023

The purpose of this program is to create a student class that inherits from the person class.

"""
from DerivedPersonStudent.Person import Person


class Student(Person):
    def __init__(self, sd, lname, fname, m="Computer Science", gpa=0.0):
        super().__init__(lname, fname)
        self._major = m
        self._student_id = sd
        self._gpa = gpa

    def change_major(self, new_major):
        self._major = new_major

    def update_gpa(self, new_gpa):
        self._gpa = new_gpa

    def display(self):
        return Person.display(self) + "Student ID: " + str(self._student_id) + "\nMajor: " + str(self._major) + ', GPA: ' + str(self._gpa) + "\n"


# Driver
if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student

"""
Testing:
Song, River
Student ID: 900111111
Major: Computer Science, GPA: 0.0

Song, River
Student ID: 900111111
Major: Computer Engineering, GPA: 0.0

Song, River
Student ID: 900111111
Major: Computer Engineering, GPA: 4.0

Process finished with exit code 0    

Testing could also be done with a unit test for the class
"""
