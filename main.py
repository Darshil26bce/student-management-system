import csv


student_file = "students.csv"
course_file = "courses.csv"
marks_file = "marks.csv"


def add_student():
    again = 1

    while again == 1:
        print()
        reg_no = input("ENTER STUDENT REGISTRATION NUMBER : ")
        print()
        name = input("ENTER STUDENT NAME : ")
        print()
        email = input("ENTER STUDENT EMAIL ID : ")
        print()
        branch = input("ENTER STUDENT DEPARTMENT : ")
        print()
        year = input("ENTER STUDENT ENROLLMENT YEAR : ")

        file = open(student_file, "a", newline="")
        writer = csv.writer(file)
        writer.writerow([reg_no, name, email, branch, year])
        file.close()

        print()
        print("STUDENT ADDED SUCCESSFULLY")
        print()

        again = int(input(
            "ENTER 1 TO ADD ANOTHER STUDENT OR 0 TO RETURN : "
        ))


def show_students():
    print()
    print("================ STUDENT LIST ================")

    try:
        file = open(student_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                print("STUDENT ID :", row[0])
                print("NAME       :", row[1])
                print("EMAIL      :", row[2])
                print("DEPARTMENT :", row[3])
                print("BATCH      :", row[4])
                print("---------------------------------------")

        file.close()

    except FileNotFoundError:
        print("NO STUDENT DATA FOUND")


def find_student():
    print()
    wanted_id = input("ENTER STUDENT ID TO SEARCH : ")
    found = 0

    try:
        file = open(student_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                if row[0] == wanted_id:
                    print()
                    print("                STUDENT FOUND")
                    print("-----------------------------------------------")
                    print("STUDENT ID :", row[0])
                    print("NAME       :", row[1])
                    print("EMAIL      :", row[2])
                    print("DEPARTMENT :", row[3])
                    print("BATCH      :", row[4])
                    found = 1
                    break

        file.close()

    except FileNotFoundError:
        found = 0

    if found == 0:
        print()
        print("STUDENT NOT FOUND")


def students_menu():
    while True:
        print()
        print("================ MANAGE STUDENTS ================")
        print()
        print("1. ADD STUDENT")
        print()
        print("2. VIEW STUDENTS")
        print()
        print("3. SEARCH STUDENT")
        print()
        print("4. BACK TO MAIN MENU")
        print()

        option = int(input("ENTER YOUR CHOICE : "))

        if option == 1:
            add_student()

        elif option == 2:
            show_students()

        elif option == 3:
            find_student()

        elif option == 4:
            print()
            print("GOING BACK TO MAIN MENU")
            break

        else:
            print("INVALID CHOICE")


def add_course():
    print()
    code = input("ENTER COURSE ID : ")
    print()
    title = input("ENTER COURSE NAME : ")
    print()
    dept = input("ENTER DEPARTMENT : ")
    print()
    credit = input("ENTER CREDITS : ")

    file = open(course_file, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([code, title, dept, credit])
    file.close()

    print("COURSE ADDED SUCCESSFULLY")


def show_courses():
    print()
    print("================ COURSE LIST ================")

    try:
        file = open(course_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "course_id":
                print("COURSE ID   :", row[0])
                print("COURSE NAME :", row[1])
                print("DEPARTMENT  :", row[2])
                print("CREDITS     :", row[3])
                print("---------------------------------------------")

        file.close()

    except FileNotFoundError:
        print("NO COURSE DATA FOUND")


def courses_menu():
    while True:
        print()
        print("================ MANAGE COURSES ================")
        print()
        print("1. ADD COURSE")
        print()
        print("2. VIEW COURSES")
        print()
        print("3. BACK TO MAIN MENU")
        print()

        option = int(input("ENTER YOUR CHOICE : "))

        if option == 1:
            add_course()

        elif option == 2:
            show_courses()

        elif option == 3:
            print()
            print("GOING BACK TO MAIN MENU")
            break

        else:
            print("INVALID CHOICE")


def check_student(student_no):
    try:
        file = open(student_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                if row[0] == student_no:
                    file.close()
                    return 1

        file.close()

    except FileNotFoundError:
        return 0

    return 0


def check_course(course_no):
    try:
        file = open(course_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "course_id":
                if row[0] == course_no:
                    file.close()
                    return 1

        file.close()

    except FileNotFoundError:
        return 0

    return 0


def add_marks():
    print()
    print("================ ENTER MARKS ================")

    student_no = input("ENTER STUDENT ID : ")
    subject_code = input("ENTER COURSE ID : ")
    score = int(input("ENTER MARKS : "))

    if check_student(student_no) == 0:
        print("STUDENT NOT FOUND")
        print("RETURNING TO MAIN MENU")
        return

    if check_course(subject_code) == 0:
        print("COURSE NOT FOUND")
        print("RETURNING TO MAIN MENU")
        return

    if score < 0 or score > 100:
        print("MARKS SHOULD BE BETWEEN 0 AND 100")
        return

    file = open(marks_file, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([student_no, subject_code, score])
    file.close()

    print("MARKS ENTERED SUCCESSFULLY")
    print("RETURNING TO MAIN MENU")


def get_student(student_no):
    try:
        file = open(student_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                if row[0] == student_no:
                    file.close()
                    return row

        file.close()

    except FileNotFoundError:
        return None

    return None


def get_marks(student_no):
    all_marks = []

    try:
        file = open(marks_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                if row[0] == student_no:
                    all_marks.append([row[1], int(row[2])])

        file.close()

    except FileNotFoundError:
        pass

    return all_marks


def get_grade(value):
    if value >= 90:
        return "A+"
    elif value >= 80:
        return "A"
    elif value >= 70:
        return "B"
    elif value >= 60:
        return "C"
    elif value >= 50:
        return "D"
    else:
        return "F"


def show_student_report():
    student_no = input("ENTER STUDENT ID : ")
    details = get_student(student_no)

    if details is None:
        print()
        print("STUDENT NOT FOUND")
        print()
        print("RETURNING TO MAIN MENU")
        return

    print()
    print("================ STUDENT REPORT ================")
    print("STUDENT ID   :", student_no)
    print()
    print("STUDENT NAME :", details[1])
    print()
    print("STUDENT EMAIL :", details[2])
    print()
    print("STUDENT BRANCH :", details[3])
    print()
    print("STUDENT ENROLLMENT YEAR :", details[4])
    print()
    print("-----------------------------------------------")

    marks = get_marks(student_no)

    if len(marks) == 0:
        print("NO MARKS ENTERED")
        return

    total_marks = 0

    for item in marks:
        print("COURSE ID :", item[0])
        print()
        print("MARKS     :", item[1])
        print("-----------------------------------------------")
        total_marks += item[1]

    number_of_subjects = len(marks)
    percentage = total_marks / number_of_subjects
    grade = get_grade(percentage)

    print("TOTAL MARKS :", total_marks)
    print()
    print("PERCENTAGE  :", percentage)
    print()
    print("GRADE       :", grade)
    print("-----------------------------------------------")


def show_average():
    total_marks = 0
    number = 0

    try:
        file = open(marks_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                total_marks += int(row[2])
                number += 1

        file.close()

    except FileNotFoundError:
        number = 0

    if number == 0:
        print("NO MARKS AVAILABLE")
        return

    average = total_marks / number

    print()
    print("============== CLASS AVERAGE ==============")
    print("CLASS AVERAGE :", average)
    print()
    print("RETURNING TO MAIN MENU")
    print("-----------------------------------------------")


def show_top_students():
    students = []

    try:
        file = open(student_file, "r")
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != "student_id":
                student_no = row[0]
                student_name = row[1]
                marks = get_marks(student_no)

                if len(marks) > 0:
                    total = 0

                    for mark in marks:
                        total += mark[1]

                    percentage = total / len(marks)
                    students.append([student_no, student_name, percentage])

        file.close()

    except FileNotFoundError:
        pass

    # Sort students according to their percentage.
    students.sort(key=lambda x: x[2], reverse=True)

    print()
    print("=============== TOP PERFORMERS ===============")

    if len(students) == 0:
        print("NO MARKS AVAILABLE")
        return

    position = 1

    for student in students:
        if position > 5:
            break

        print()
        print("RANK       :", position)
        print("STUDENT ID :", student[0])
        print("NAME       :", student[1])
        print("PERCENTAGE :", student[2])
        print("---------------------------------------------")

        position += 1


def reports_menu():
    while True:
        print()
        print("================ VIEW REPORTS ================")
        print()
        print("1. STUDENT REPORT")
        print()
        print("2. CLASS AVERAGE")
        print()
        print("3. TOP PERFORMERS")
        print()
        print("4. BACK TO MAIN MENU")
        print()

        option = int(input("ENTER YOUR CHOICE : "))
        print()

        if option == 1:
            show_student_report()

        elif option == 2:
            show_average()

        elif option == 3:
            show_top_students()

        elif option == 4:
            print("GOING BACK TO MAIN MENU")
            break

        else:
            print("INVALID CHOICE")


def start_program():
    active = 1

    print("HELLO !")
    print("==================================================================================================================================")
    print("                                                 STUDENT MANAGEMENT SYSTEM")
    print("==================================================================================================================================")

    while active == 1:
        print()
        print("1. MANAGE STUDENTS")
        print()
        print("2. MANAGE COURSES")
        print()
        print("3. ENTER MARKS")
        print()
        print("4. VIEW REPORTS")
        print()
        print("5. EXIT")
        print()

        choice = int(input("ENTER YOUR CHOICE FROM ABOVE : "))

        if choice == 1:
            students_menu()

        elif choice == 2:
            courses_menu()

        elif choice == 3:
            add_marks()

        elif choice == 4:
            reports_menu()

        elif choice == 5:
            print()
            print("THANK YOU FOR USING STUDENT MANAGEMENT SYSTEM")
            active = 0

        else:
            print("INVALID CHOICE")


start_program()