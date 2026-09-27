class University:

    university_name = "Codegnan University"

    total_students = 0
    total_courses = 0
    total_faculty = 0

    def __init__(self):

        self.students = {}
        self.courses = {}
        self.faculties = {}

    def add_student(self, student):

        self.students[student.student_id] = {
            "Name": student.name,
            "Age": student.age,
            "Student ID": student.student_id,
            "Year": student.Year_,
            "Education": student.Edu_BG,
            "Gender": student.Gender,
            "Department": student.Department,
            "Courses": student.courses
        }

        University.total_students += 1

    def add_course(self, course):

        self.courses[course.course_id] = {
            "Course Name": course.course_name,
            "Course ID": course.course_id,
            "Schedule": course.schedule
        }

        University.total_courses += 1

    def add_faculty(self, faculty):

        self.faculties[faculty.faculty_id] = {
            "Name": faculty.name,
            "Age": faculty.age,
            "Faculty ID": faculty.faculty_id,
            "Education": faculty.Edu_BG,
            "Gender": faculty.Gender,
            "Department": faculty.Department
        }

        University.total_faculty += 1

    def view_students(self):

        print("\n------ All Students ------")

        for student_id, student in self.students.items():

            print("\nStudent ID :", student_id)

            for key, value in student.items():
                print(key, ":", value)

    def view_courses(self):

        print("\n------ All Courses ------")

        for course_id, course in self.courses.items():

            print("\nCourse ID :", course_id)

            for key, value in course.items():
                print(key, ":", value)

    def view_faculty(self):

        print("\n------ All Faculty ------")

        for faculty_id, faculty in self.faculties.items():

            print("\nFaculty ID :", faculty_id)

            for key, value in faculty.items():
                print(key, ":", value)


class Student:

    def __init__(self, university, name, age, student_id, Year_, Edu_BG, Gender, Department):

        self.name = name
        self.age = age
        self.student_id = student_id
        self.Year_ = Year_
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

        self.courses = []

        university.add_student(self)

    def display_student(self):

        print("\n------ Student Details ------")

        print("University :", University.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.student_id)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def enroll(self, course):

        self.courses.append(course)

        course.students[self.student_id] = {
            "Name": self.name,
            "Age": self.age,
            "Student ID": self.student_id,
            "Year": self.Year_,
            "Education": self.Edu_BG,
            "Gender": self.Gender,
            "Department": self.Department
        }

        print(self.name, "enrolled in", course.course_name)

    def view_courses(self):

        print("\n------ Courses Enrolled ------")

        print("Student :", self.name)

        for course in self.courses:
            print(course.course_name)


class Course:

    def __init__(self, university, course_id, course_name, schedule):

        self.course_id = course_id
        self.course_name = course_name
        self.schedule = schedule

        self.students = {}

        university.add_course(self)

    def display_course(self):

        print("\n------ Course Details ------")

        print("University  :", University.university_name)
        print("Course ID   :", self.course_id)
        print("Course Name :", self.course_name)
        print("Schedule    :", self.schedule)

    def view_students(self, course_id):

        if self.course_id == course_id:

            print("\n------ Course Students ------")

            print("Course ID      :", self.course_id)
            print("Course         :", self.course_name)
            print("Total Students :", len(self.students))

            for student_id, student in self.students.items():

                print("\nStudent ID :", student_id)

                for key, value in student.items():
                    print(key, ":", value)

        else:

            print("Course ID not found")


class Faculty:

    def __init__(self, university, name, age, faculty_id, Department, Edu_BG, Gender):

        self.name = name
        self.age = age
        self.faculty_id = faculty_id
        self.Department = Department
        self.Edu_BG = Edu_BG
        self.Gender = Gender

        self.courses = []

        university.add_faculty(self)

    def display_faculty(self):

        print("\n------ Faculty Details ------")

        print("University  :", University.university_name)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Faculty ID  :", self.faculty_id)
        print("Education   :", self.Edu_BG)
        print("Gender      :", self.Gender)
        print("Department  :", self.Department)

    def manage_course(self, course):

        self.courses.append(course)

        print(
            self.name,
            "is handling",
            course.course_name
        )

    def view_courses(self):

        print("\n------ Faculty Courses ------")

        print("Faculty :", self.name)

        for course in self.courses:
            print(course.course_name)


university = University()


faculty1 = Faculty(
    university,
    "Ravi",
    35,
    "F101",
    "CSE",
    "M.Tech",
    "Male"
)


faculty2 = Faculty(
    university,
    "Priya",
    32,
    "F102",
    "ECE",
    "M.Tech",
    "Female"
)


course1 = Course(
    university,
    "C101",
    "Python",
    "Monday 10 AM"
)


course2 = Course(
    university,
    "C102",
    "SQL",
    "Tuesday 11 AM"
)


faculty1.manage_course(course1)
faculty1.manage_course(course2)


student1 = Student(
    university,
    "Narasimha",
    22,
    "ST101",
    "4th Year",
    "B.Tech",
    "Male",
    "CSE"
)


student2 = Student(
    university,
    "Rahul",
    21,
    "ST102",
    "3rd Year",
    "B.Tech",
    "Male",
    "ECE"
)


student1.enroll(course1)
student1.enroll(course2)

student2.enroll(course1)


student1.view_courses()

faculty1.view_courses()

course1.view_students("C101")

course2.view_students("C102")

university.view_students()
university.view_courses()
university.view_faculty()
print("total no of students:",university.total_students)










            
