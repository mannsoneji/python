# What relationship is appropriate for Course and Faculty?

# In the context of Object-Oriented Programming (OOP) and modeling real-world entities, the relationship between a Course and Faculty is typically a "teaches" or "teaching" relationship. This is because a Faculty member is responsible for teaching a Course.

class Faculty:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)

    def get_courses(self):
        return [course.name for course in self.courses]
    
class Course:
    def __init__(self,name,faculty):
        self.name = name
        self.faculty = faculty

faculty = input("Enter a faculty name : ")
faculty1 = Faculty(faculty)


course1 = Course("Python",faculty1)
course2 = Course("Data Science",faculty1)


faculty1.add_courses(course1)
faculty1.add_courses(course2)

print(faculty1.name + " teaches:", faculty1.get_courses())