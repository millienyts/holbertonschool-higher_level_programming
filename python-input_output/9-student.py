#!/usr/bin/python3
"""
Student module
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__


if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]
    for student in students:
        j_student = student.to_json()
        print(j_student['first_name'])
        print(j_student['age'])
