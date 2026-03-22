class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)


manager1 = Manager("Tanvi", 19, 101, 50000, "CSE")

manager1.display()
