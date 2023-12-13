class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def get_info(self):
        super().get_info()
        print(f"Студенческий ID: {self.student_id}, Специальность: {self.major}")


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, department):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.department = department

    def get_info(self):
        super().get_info()
        print(f"ID преподавателя: {self.teacher_id}, Кафедра: {self.department}")


class DepartmentHead(Teacher):
    def __init__(self, name, age, gender, teacher_id, department, department_name):
        super().__init__(name, age, gender, teacher_id, department)
        self.department_name = department_name

    def get_info(self):
        super().get_info()
        print(f"Название кафедры: {self.department_name}")
