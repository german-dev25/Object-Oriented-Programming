"""
Базовое задние:
1) Переписать код в соответствии с Single Responsibility Principle:
public class Employee {
    private String name;
    private Date dob;
    private int baseSalary;
    public Employee(String name, Date dob, int baseSalary) {
        this.name = name;
        this.dob = dob;
        this.baseSalary = baseSalary;
    }
    public String getEmpInfo() {
        return "name - " + name + " , dob - " + dob.toString();
    }
    public int calculateNetSalary() {
        int tax = (int) (baseSalary * 0.25);//calculate in otherway
        return baseSalary - tax;
    }
}
Подсказка: вынесите метод calculateNetSalary() в отдельный класс
"""
from datetime import date


# Класс Employee отвечает только за данные, касающиеся непосредственно
# каждого Employee. Класс EmployeeSalaryCalculator при инициализации получает
# значение tax, а при вызове получает объект Employee и считает для него
# итоговую чистую зарплату. Каждый класс выполняет только задачу определенного
# направления.
class Employee:
    def __init__(self, name: str, dob: date, base_salary: int):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def __str__(self) -> str:
        return f'name - {self.name}, dob - {self.dob.strftime("%Y-%m-%d")}'


class EmployeeSalaryCalculator:
    def __init__(self, tax: float):
        self.tax = tax

    def __call__(self, emp: Employee) -> int:
        return int(emp.base_salary * (1 - self.tax))


salary_calculator_025 = EmployeeSalaryCalculator(tax=0.25)

employee_data = [
    ("Vadim Ivanov", date(1990, 5, 15), 50000),
    ("Nikolai Petrov", date(1988, 8, 25), 60000),
    ("Igor Nikolaev", date(1995, 3, 10), 55000)
]

for employee_info in employee_data:
    employee = Employee(*employee_info)
    print(f'{employee} - net salary {salary_calculator_025(employee)}')
