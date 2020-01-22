class Student:
    def __init__(self, id, marks, age):
        self.id=id
        self.marks=marks
        self.age=age

    def validate_marks(self,marks):
        if self.marks>=0 and self.marks<=100:
            return True
    def validate_age(self):
        if self.age>20:
            return True
    def check_qualification(self, marks, age):
        if self.marks>=65 and self.marks<=100 and self.age>20:
            return True
        else:
            return False

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

    def set_student_id(self,id ):
        self.id = id

    def get_student_id(self):
        return self.id

    def set_age(self, age):
        self.age=age

    def get_age(self):
        return self.age



s1=Student(52999, 63, 22)
s1.check_qualification(66,20)
s1.set_marks(100)
print (s1.validate_marks(50))
