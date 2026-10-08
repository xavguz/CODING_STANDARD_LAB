"""Module that represents students"""

class Student:
    """Represents a student"""
    def __init__(self, student_id, name):
        """Initializes a student"""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Adds a grade to the student's list."""
        if not isinstance(grade, (int, float)):
            raise TypeError("The grade must be a number.")
        if grade < 0 or grade > 100:
            raise ValueError("The grade must be between 0 and 100.")
        self.grades.append(grade)

    def calculate_average(self):
        """Calculates the average grade of the student"""
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        """Checks whether the student qualifies for honors"""
        if self.calculate_average() > 90:
            self.honor = True

    def delete_grade(self, index):
        """Deletes a grade from the student's list."""
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        if index < 0 or index >= len(self.grades):
            raise IndexError("The grade index does not exist.")
        del self.grades[index]

    def report(self):
        """Prints a report with the student's information."""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade: {self.calculate_average()}")


def startrun():
    """Runs a test scenario for the Student class"""
    a = Student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")  # broken
    a.calculate_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
