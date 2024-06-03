class Student:
    name="Raziah"
    code="004"
    school="AkiraChix"
    age=20

class Students:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.code=code
    def greet_student(self):
        greeting=f"Hello {self.first_name},welcome to {self.school}.Your code is {self.code}"
        return greeting
    def greet_student_by_age(self):
        greeting=f"Hello {self.age}"
        return greeting
    def display_intials(self):
        greeting=f"Hello {self.first_name[0]}{self.last_name[0]}"
        return greeting
    def display_full_name(self):
        greeting=f"{self.first_name} {self.last_name}"
        return greeting
    def enroll(self):
        greeting=f"{self.school}"

