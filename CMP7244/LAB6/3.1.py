class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_profile_info(self):
        return "Name: %s, Phone number: %s" % (self.name, self.phone_number)


class Student(Person):

    def __init__(self, course, *args, **kwargs):
        self.course = course
        self.classes = []
        super().__init__(*args, **kwargs)

    def enrol(self, module):
        self.classes.append(module)


class StaffMember(Person):

    def __init__(self, salary, *args, **kwargs):
        self.courses = []
        self.salary = salary
        super().__init__(*args, **kwargs)

    def administrator_for(self, module):
        self.courses.append(module)

    def get_salary(self):
        return "Salary : %s" % (self.salary)


class Lecturer(StaffMember):

    def __init__(self, academic_title, *args, **kwargs):
        self.academic_title = academic_title
        super().__init__(*args, **kwargs)

    def lect_info(self):
        return "academic_title : %s" % (self.academic_title)


def main():
    L1 = Lecturer('Professor', name='Harsha',
                  phone_number='123456789', salary='30000')
    print(L1.get_profile_info(),
          L1.get_salary(),
          L1.lect_info())


main()
