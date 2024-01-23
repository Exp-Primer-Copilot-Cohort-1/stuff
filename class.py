# class Student:
#     def __init__(self, first_name, last_name, subject, grade, attendance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.subject = subject
#         self.grade = grade
#         self.attendance = attendance

# def create_student_list():
#     students = [
#         Student("John", "James", "CS", "A", "100"),
#         Student("Alice", "Smith", "CS", "A", "50"),
#         Student("Hassan", "Ali", "CS", "A", "100"),
#         Student("Alice", "Smith", "Maths", "B", "90"),
#         Student("John", "James", "Maths", "C", "75"),
#     ]
#     return students

# def display_students(students):
#     print("Students in Computer Science:")
#     print("First Name\tLast Name\tSubject\t\tGrade\t\tAttendance")
#     for student in students:
#         if student.subject == "CS":
#             if int(student.attendance) < 100:
#                 print(f"{student.first_name}\t\t{student.last_name}\t\t{student.subject}\t\t{student.grade}\t\t{student.attendance} ALERT")
#             else:

#                 print(f"{student.first_name}\t\t{student.last_name}\t\t{student.subject}\t\t{student.grade}\t\t{student.attendance}")

# students = create_student_list()
# display_students(students)

class Student:

    def __init__(self, first_name, last_name, subject, grade, attendance):

        self.first_name = first_name

        self.last_name = last_name

        self.subject = subject

        self.grade = grade

        self.attendance = attendance

def create_student_list():

    students = [

        Student("John", "James", "CS", "A", 100),

        Student("Alice", "Smith", "CS", "A", 50),

        Student("Hassan", "Ali", "CS", "A", 100),

        Student("Alice", "Smith", "Maths", "B", 90),

        Student("John", "James", "Maths", "C", 75),

    ]

    return students

def display_students(students):

    cs_attendance = {}

    math_attendance = {}

    total_attendance = 0

    total_students_count = 0

    for student in students:
        if student.subject == "CS":

            print(f"\nDetails for {student.first_name} {student.last_name}:")
            
        print(f"Subject: {student.subject}, Grade: {student.grade}, Attendance: {student.attendance}%")

        # Calculate and display average attendance for CS and Math

        if student.subject == "CS":

            cs_attendance[student.first_name] = cs_attendance.get(student.first_name, []) + [student.attendance]

        elif student.subject == "Maths":

            math_attendance[student.first_name] = math_attendance.get(student.first_name, []) + [student.attendance]

        # Calculate general attendance

        if student.attendance > 0:

            total_attendance += student.attendance

            total_students_count += 1

    if total_students_count > 0:

        general_average_attendance = total_attendance / total_students_count

        print(f"\nGeneral Average Attendance: {general_average_attendance}%")

    print("\nAverage Attendance for CS students:")

    for name, attendance_list in cs_attendance.items():

        average_attendance = sum(attendance_list) / len(attendance_list)

        print(f"{name}: {average_attendance}%")

students_list = create_student_list()

display_students(students_list)