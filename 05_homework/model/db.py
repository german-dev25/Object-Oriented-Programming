from model.student import Student

""" Услованая БД со студентами """
students_list = [Student(name='Иван', age=25, student_id=121),
                 Student(name='Игорь', age=23, student_id=301),
                 Student(name='Иван', age=22, student_id=123),
                 Student(name='Игорь', age=23, student_id=444),
                 Student(name='Даша', age=24, student_id=171),
                 Student(name='Лена', age=23, student_id=104)]

students_for_dict = [Student(name='Коля', age=25, student_id=122),
                     Student(name='Саша', age=23, student_id=101),
                     Student(name='Юля', age=25, student_id=105),
                     Student(name='Лена', age=22, student_id=500)]
students_dict = {}

for student in students_for_dict:
    students_dict[student.student_id] = student
