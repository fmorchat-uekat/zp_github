class Student:
    name: str
    marks: list

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        if avg > 50:
            return 1
        return 0
