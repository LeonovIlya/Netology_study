class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        data_avg_grade = []
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            data_avg_grade.append(res)
        finaly_res = sum(data_avg_grade) / len(data_avg_grade)
        return round(finaly_res, 2)

    def __str__(self):
        res = f'''
              Имя: {self.name}
              Фамилия: {self.surname}
              Средняя оценка за домашние задания: {self.avg_grade()}
              Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
              Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_grade() < other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade_lecturer(self):
        data_avg_grade = []
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            data_avg_grade.append(res)
        finaly_res = sum(data_avg_grade) / len(data_avg_grade)
        return round(finaly_res, 2)

    def __str__(self):
        res = f'''
              Имя: {self.name}
              Фамилия: {self.surname}
              Средняя оценка за лекции: {self.avg_grade_lecturer()}'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avg_grade_lecturer() < other.avg_grade_lecturer()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''
              Имя: {self.name}
              Фамилия: {self.surname}'''
        return res


def avg_all_students(student_list, course):
    data_avg_grade = []
    for name, grades in student_list.items():
        for course_name, grade in grades.items():
            if course_name == course:
                res = sum(grade) / len(grade)
                data_avg_grade.append(res)
    finaly_res = round(sum(data_avg_grade) / len(data_avg_grade), 2)
    return f'Средняя оценка за ДЗ по курсу {course} - {finaly_res}'


def avg_all_lecturer(lecturer_list, course):
    data_avg_grade = []
    for name, grades in lecturer_list.items():
        for course_name, grade in grades.items():
            if course_name == course:
                res = sum(grade) / len(grade)
                data_avg_grade.append(res)
    finaly_res = round(sum(data_avg_grade) / len(data_avg_grade), 2)
    return f'Средняя оценка за лекции по курсу {course} - {finaly_res}'


some_student1 = Student('Ruoy', 'Eman', 'male')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.courses_in_progress += ['HTML']
some_student1.finished_courses += ['Java']
some_student1.finished_courses += ['CSS']
some_student1.grades['Git'] = [10, 10, 9, 10, 10, 6, 5]
some_student1.grades['Python'] = [10, 9, 10, 10, 4, 5, 2, 3, 2, 8, 8]

some_student2 = Student('Mike', 'Pupkin', 'male')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Java']
some_student2.finished_courses += ['CSS']
some_student2.finished_courses += ['HTML']
some_student2.grades['Git'] = [8, 6, 9, 7, 10, 10, 10, 9]
some_student2.grades['Python'] = [4, 9, 7, 10, 4, 10, 10, 6, 2, 8, 8]

some_lecturer1 = Lecturer('Sponge', 'Bob')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Git']
some_lecturer1.grades['Python'] = [10, 9, 4, 5, 2, 3, 2, 8, 8]
some_lecturer1.grades['Git'] = [10, 10, 9, 10, 10]

some_lecturer2 = Lecturer('Mister', 'Crabs')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['HTML']
some_lecturer2.courses_attached += ['Git']
some_lecturer2.grades['Python'] = [8, 9, 9, 10, 4, 5, 7, 3, 5, 8, 8]
some_lecturer2.grades['Git'] = [10, 10, 9, 10, 10, 5, 8, 10, 4, 6]

some_reviewer = Reviewer('Someone', 'Buddymen')

all_students_grades = {'Ruoy Eman': {'Git': [10, 10, 9, 10, 10, 6, 5],
                                     'Python': [10, 9, 10, 10, 4, 5, 2, 3, 2, 8, 8]},

                       'Mike Pupkin': {'Git': [8, 6, 9, 7, 10, 10, 10, 9],
                                       'Python': [4, 9, 7, 10, 4, 10, 10, 6, 2, 8, 8]}}

all_lecturer_grades = {'Sponge Bob': {'Git': [10, 10, 9, 10, 10],
                                      'Python': [10, 9, 4, 5, 2, 3, 2, 8, 8]},

                       'Mister Crabs': {'Git': [10, 10, 9, 10, 10, 5, 8, 10, 4, 6],
                                        'Python': [8, 9, 9, 10, 4, 5, 7, 3, 5, 8, 8]}}

print(some_reviewer)

print(some_student1)

print(some_lecturer1)

print(some_lecturer1.avg_grade_lecturer())
some_student1.rate_lecturer(some_lecturer1, 'Git', 5)
print(some_lecturer1.avg_grade_lecturer())

print(some_student1.avg_grade())
some_reviewer.rate_hw(some_student1, 'Git', 1)
print(some_student1.avg_grade())

print(some_student1 > some_student2)
print(some_lecturer1 > some_lecturer2)

print(avg_all_students(all_students_grades, 'Git'))
print(avg_all_students(all_students_grades, 'Python'))

print(avg_all_lecturer(all_lecturer_grades, 'Git'))
print(avg_all_lecturer(all_lecturer_grades, 'Python'))
