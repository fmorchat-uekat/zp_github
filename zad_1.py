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

s1 = Student("Aneta",[55,80,40,97])
s2 = Student("Antek",[90,10,30,67])

print(s1.is_passed())
print(s2.is_passed())