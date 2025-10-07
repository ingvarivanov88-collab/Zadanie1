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

    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_rating(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_rating = self.get_average_rating()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_rating:.1f}")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_rating() == other.get_average_rating()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_rating() < other.get_average_rating()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функции для подсчета средних оценок
def calculate_average_hw_grade(students, course):
    total_grade = 0
    count = 0

    for student in students:
        if course in student.grades and student.grades[course]:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])

    return total_grade / count if count > 0 else 0

# Функция для подсчета средних оценок за лекции
def calculate_average_lecture_grade(lecturers, course):
    total_grade = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.grades and lecturer.grades[course]:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])

    return total_grade / count if count > 0 else 0


if __name__ == "__main__":
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Петр', 'Петров')

    reviewer1 = Reviewer('Сергей', 'Сергеев')
    reviewer2 = Reviewer('Анна', 'Аннова')

    student1 = Student('Ольга', 'Алёхина', 'Ж')
    student2 = Student('Алексей', 'Алексеев', 'М')

    lecturer1.courses_attached += ['Python', 'C++']
    lecturer2.courses_attached += ['Python', 'Java']
    reviewer1.courses_attached += ['Python', 'C++']
    reviewer2.courses_attached += ['Java']
    student1.courses_in_progress += ['Python', 'Java']
    student2.courses_in_progress += ['Python']
    student1.finished_courses += ['Введение в программирование']
    student2.finished_courses += ['Git основы']

    student1.rate_lecturer(lecturer1, 'Python', 9)
    student1.rate_lecturer(lecturer1, 'Python', 8)
    student2.rate_lecturer(lecturer1, 'Python', 10)

    student1.rate_lecturer(lecturer2, 'Python', 7)
    student1.rate_lecturer(lecturer2, 'Python', 6)

    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student2, 'Python', 10)
    reviewer2.rate_hw(student1, 'Java', 7)

    print(reviewer1)
    print()
    print(reviewer2)
    print()

    print(lecturer1)
    print()
    print(lecturer2)
    print()

    print(student1)
    print()
    print(student2)
    print()

    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
    print()

    print(f"student1 > student2: {student1 > student2}")
    print(f"student1 < student2: {student1 < student2}")
    print(f"student1 == student2: {student1 == student2}")

    # Демонстрация работы функций для подсчета средних оценок
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    # Средняя оценка за домашние задания по курсу Python
    avg_hw_python = calculate_average_hw_grade(students_list, 'Python')
    print(f"\nСредняя оценка за домашние задания по курсу 'Python': {avg_hw_python:.1f}")

    # Средняя оценка за домашние задания по курсу Java
    avg_hw_java = calculate_average_hw_grade(students_list, 'Java')
    print(f"Средняя оценка за домашние задания по курсу 'Java': {avg_hw_java:.1f}")

    # Средняя оценка за лекции по курсу Python
    avg_lecture_python = calculate_average_lecture_grade(lecturers_list, 'Python')
    print(f"Средняя оценка за лекции по курсу 'Python': {avg_lecture_python:.1f}")

    # Средняя оценка за лекции по курсу Java
    avg_lecture_java = calculate_average_lecture_grade(lecturers_list, 'Java')
    print(f"Средняя оценка за лекции по курсу 'Java': {avg_lecture_java:.1f}")