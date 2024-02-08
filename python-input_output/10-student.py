#!/usr/bin/python3
"""
Student module with filter
"""


class Student:
    """
    Student class with filter
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    print(student_1.to_json())
    print(student_2.to_json(['first_name', 'age']))
    print(student_2.to_json(['middle_name', 'age']))
