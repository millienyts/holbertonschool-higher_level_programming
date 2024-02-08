#!/usr/bin/python3
"""
Student module with disk reload
"""


class Student:
    """
    Student class with disk reload
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(student_1.first_name, student_1.last_name, student_1.age)

    save_to_json_file(j_student_1, "student.json")
    read_file("student.json")
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(new_student_1.first_name, new_student_1.last_name, new_student_1.age)

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file("student.json")

    new_student_1.reload_from_json(new_j_student_1)
    print(new_student_1)
    print(new_student_1.first_name, new_student_1.last_name, new_student_1.age)
