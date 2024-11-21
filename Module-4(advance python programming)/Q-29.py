# What relationship is appropriate for Student and Person?

# In Object-Oriented Programming (OOP) and real-world modeling, the relationship between Student and Person is typically a "is-a" relationship, meaning that a Student is a type of Person. This is a classic example of inheritance, where the Student class is a subclass of the Person class


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def intro(self):
        print(f"Hi,I am {self.name} and I am {self.age} years old") 

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age) 
        self.student_id = student_id


    def intro(self):
        super().intro()
        print(f"I am a student, and my student ID is {self.student_id}.")

student = Student("Mann Soneji", 21, "21072004")

student.intro()