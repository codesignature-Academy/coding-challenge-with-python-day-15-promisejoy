class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")
book1 = Book("Techrise cohort2", "Smart", 328)
book1.info()
book2 = Book("Python crash course", "Promise", 281)
book2.info()







class Student:
    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
    
    def description(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Score: {self.score}"

student1 = Student("Prospect", "#555", 85)
student2 = Student("Smart", "#444", 92)

print(student1.description())
print(student2.description())