from controllers.employee_controller import EmployeeController
from controllers.student_controller import StudentController
from controllers.teacher_controller import TeacherController
from domen.employee import Employee
from domen.student import Student
from domen.teacher import Teacher

#
# st_4580_1 = Student(name='Иван', age=25, student_id=121)
# st_4580_2 = Student(name='Игорь', age=23, student_id=301)
# st_4580_3 = Student(name='Иван', age=22, student_id=123)
# st_4580_4 = Student(name='Игорь', age=23, student_id=444)
# st_4580_5 = Student(name='Даша', age=23, student_id=171)
# st_4580_6 = Student(name='Лена', age=23, student_id=104)
#
# st_4581_1 = Student(name='Коля', age=25, student_id=122)
# st_4581_2 = Student(name='Саша', age=23, student_id=101)
# st_4581_3 = Student(name='Юля', age=25, student_id=105)
# st_4581_4 = Student(name='Лена', age=22, student_id=500)
#
# st_4582_1 = Student(name='Оля', age=22, student_id=125)
# st_4582_2 = Student(name='Ваня', age=24, student_id=99)
# st_4582_3 = Student(name='Саша', age=21, student_id=108)
# st_4582_4 = Student(name='Коля', age=24, student_id=55)
#
# st_4555_1 = Student(name='Юля', age=21, student_id=223)
# st_4555_2 = Student(name='Никита', age=23, student_id=201)
# st_4555_3 = Student(name='Юра', age=21, student_id=105)
# st_4555_4 = Student(name='Игорь', age=22, student_id=206)
# st_4555_5 = Student(name='Катя', age=22, student_id=189)
#
# st_4000_1 = Student(name='Ваня', age=23, student_id=155)
# st_4000_2 = Student(name='Лена', age=20, student_id=177)
# st_4000_3 = Student(name='Игорь', age=22, student_id=166)
# st_4000_4 = Student(name='Даша', age=21, student_id=188)
#
# group_4580 = StudentGroup(
#     group=[st_4580_1, st_4580_2, st_4580_3, st_4580_4, st_4580_5, st_4580_6],
#     group_id=4580)
#
# group_4581 = StudentGroup(
#     group=[st_4581_1, st_4581_2, st_4581_3, st_4581_4],
#     group_id=4581)
#
# group_4582 = StudentGroup(
#     group=[st_4582_1, st_4582_2, st_4582_3, st_4582_4],
#     group_id=4582)
#
# group_4555 = StudentGroup(
#     group=[st_4555_1, st_4555_2, st_4555_3, st_4555_4, st_4555_5],
#     group_id=4555)
#
# group_4000 = StudentGroup(
#     group=[st_4000_1, st_4000_2, st_4000_3, st_4000_4],
#     group_id=4000)
#
# steam_2 = StudentSteam(
#     steam=[group_4582, group_4580, group_4581],
#     steam_id=2
# )
#
# steam_5 = StudentSteam(
#     steam=[group_4555, group_4000],
#     steam_id=5
# )
#
# print('===================Группа без сортировки===================')
# for student in group_4580:
#     print(student)
#
# print('===================Группа без сортировки===================')
# for student in group_4000:
#     print(student)
#
# print('===================Группа с сортировкой====================')
# for student in sorted(group_4580):
#     print(student)
#
# print('===================Группа с сортировкой====================')
# for student in sorted(group_4000):
#     print(student)
#
# print('====================Поток без сортировки===================')
# print(f'Поток №{steam_2.get_steam_id()}')
# for group in steam_2:
#     print(group)
#
# print('====================Поток с сортировкой====================')
# print(f'Поток №{steam_2.get_steam_id()}')
# for group in sorted(steam_2):
#     print(group)
#
# print('====================Печать всего потока====================')
# print(steam_2)
#
# print('====================Поток без сортировки===================')
# print(f'Поток №{steam_5.get_steam_id()}')
# for group in steam_5:
#     print(group)
#
# print('====================Поток с сортировкой====================')
# print(f'Поток №{steam_5.get_steam_id()}')
# for group in sorted(steam_5):
#     print(group)
#
# print('====================Печать всего потока====================')
# print(steam_5)
#

# teacher_1 = Teacher('Игорь', 24, 'Professor')


# Создание объекта StudentController и вызов метода create
student_controller = StudentController()

student_controller.create(first_name='Игорь', age=25)
student_controller.create(first_name='Иван', age=23)
student_controller.create(first_name='Даша', age=24)
student_controller.create(first_name='Лена', age=24)
student_controller.create(first_name='Юля', age=24)
student_controller.create(first_name='Коля', age=24)

# Создание объекта TeacherController и вызов метода create
teacher_controller = TeacherController()
teacher_controller.create(first_name='Николаев',
                          age=45.3,
                          acad_degree='Профессор')
teacher_controller.create(first_name='Иванов',
                          age=33.5,
                          acad_degree='Доцент')

# Создание объекта EmployeeController и вызов метода create
employee_controller = EmployeeController()
employee_controller.create(first_name='Федорович',
                           age=35,
                           special='разнорабочий')
employee_controller.create(first_name='Петрович',
                           age=24,
                           special='разнорабочий')
employee_controller.create(first_name='Иванович',
                           age=56,
                           special='разнорабочий')

# Пробуем выплатить зарплату студенту и учителю
st_4580_6 = Student(name='Ваня', age=23, student_id=155)

employee_controller.pay_salary(st_4580_6)  # Не сработает
employee_controller.pay_salary(employee_controller.emp_service.get_all()[0])

# Выплата зарплаты всем учителям
for teacher in teacher_controller.teach_service.get_all():
    teacher_controller.pay_salary(teacher)

for employee in employee_controller.emp_service.get_all():
    employee_controller.pay_salary(employee)

# Вывод в консоль списков с сортировкой
teacher_controller.teach_service.print_list()
employee_controller.emp_service.print_list()
student_controller.data_service.print_list()

# Вывод всех средних возрастов
employee_controller.emp_service.print_average()
student_controller.data_service.print_average()
teacher_controller.teach_service.print_average()
