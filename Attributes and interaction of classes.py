class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):

            if 1 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка: оценка должна быть от 1 до 10'
        else:
            return 'Ошибка: невозможно поставить оценку'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_rating(self, course=None):
        if not self.grades:
            return 0

        if course:
            if course in self.grades:
                grades_list = self.grades[course]
                return sum(grades_list) / len(grades_list)
            else:
                return 0
        else:
            all_grades = []
            for course_grades in self.grades.values():
                all_grades.extend(course_grades)
            return sum(all_grades) / len(all_grades) if all_grades else 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):

            if 1 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка: оценка должна быть от 1 до 10'
        else:
            return 'Ошибка: невозможно поставить оценку'

        lecturer = Lecturer('Иван', 'Иванов')
        reviewer = Reviewer('Пётр', 'Петров')
        student = Student('Алёхина', 'Ольга', 'Ж')

        student.courses_in_progress += ['Python', 'Java']
        lecturer.courses_attached += ['Python', 'C++']
        reviewer.courses_attached += ['Python', 'C++']

        print(student.rate_lecture(lecturer, 'Python', 7))  # None
        print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
        print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
        print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

        print(lecturer.grades)  # {'Python': [7]}