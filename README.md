# Student Management System

## Introduction

This project is a Python-based program for keeping track of students, courses, and their marks.
I made it as a command-line application, so all the operations are performed by entering choices in the terminal. Instead of using a database, the program saves the information in CSV files.
The main idea of the project is to have one place where basic academic information can be added, updated, searched, and viewed.

## What Can Be Done With The Program?

After starting the program, a menu is displayed from which different operations can be selected.

### Student Details

The student section allows the user to work with student records.

Some of the available options are:

* Register a student
* Display the list of students
* Find a particular student using their ID

For every student, the program stores their ID, name, email, department, and year of enrollment.

### Course Details

Courses can also be added to the system.

For each course, the following information is stored:

* Course ID
* Course name
* Department
* Number of credits

The added courses can be viewed whenever required.

### Adding Marks

Marks can be entered after the required student and course have been added.

The program performs some checks before saving the marks. For example, it checks whether the entered student and course actually exist. It also does not accept marks outside the range of 0 to 100.

This helps prevent incorrect entries from being stored in the file.

## Reports

The report section is used to get some useful information from the stored data.

### Student Result

By selecting a student, their academic information and marks can be displayed. The report also calculates the percentage and assigns a grade.

The grades are calculated according to this range:

90 - 100    A+
80 - 89     A
70 - 79     B
60 - 69     C
50 - 59     D
Below 50    F


### Average Marks

The program can calculate the average of the marks that have been entered.

### Top Students

The system can also find the students with the highest percentages and display up to five of them.

## Data Files

No separate database is used in this project. Three CSV files are used for storing the information:

1. students.csv
2. courses.csv
3. marks.csv


The files have different purposes:

1. students.csv → student records
2. courses.csv → course records
3. marks.csv → marks entered for students

The files are automatically used by the program when data is added or read.

## Running The Program

Make sure Python 3 is installed on the computer.
The program will then show the main menu.


===============================================================
                 STUDENT MANAGEMENT SYSTEM
===============================================================

1. MANAGE STUDENTS
2. MANAGE COURSES
3. ENTER MARKS
4. VIEW REPORTS
5. EXIT


Select an option by entering its number and pressing Enter.

## Simple Example

Suppose a student with ID 101 is added to the system.


ID: 101
Name: Rahul
Email: rahul@gmail.com
Department: CSE
Year: 2026


A course can then be created and marks can be entered for Rahul.

Once the marks are saved, the report section can be used to see the result and calculated grade.

## Technologies Used

* **Python 3**
* **CSV**
* **Command Line Interface**

The project mainly uses Python's built-in csv module, so installing external packages is not required.

## Concepts Used

While developing this project, I used several basic Python concepts, including:

* Functions
* Loops
* Conditional statements
* Lists
* User input
* File handling
* CSV reading and writing
* Calculations
* Menu-driven programming

## Final Note

This project was made to practice Python programming by building something that can actually store and use data.

Working on it helped me understand how functions, conditions, loops, and file handling can work together in a single program. It also gave me an idea of how a simple academic record system can be organized without using a database.

Screenshots:

<img width="1852" height="978" alt="Screenshot 2026-09-29 143259" src="https://github.com/user-attachments/assets/2ee3b219-f4ce-4aaa-907d-f249542d9521" />

<img width="1862" height="973" alt="Screenshot 2026-09-29 143323" src="https://github.com/user-attachments/assets/c8e15e8d-b4d4-4508-927a-c3cfd711f15b" />

<img width="1847" height="965" alt="Screenshot 2026-09-29 143339" src="https://github.com/user-attachments/assets/4cf87040-9455-4594-b92f-27d6f5072f66" />

<img width="1860" height="966" alt="Screenshot 2026-09-29 143359" src="https://github.com/user-attachments/assets/388d504a-944e-48ab-98df-26e1d94c08b3" />

<img width="1858" height="966" alt="Screenshot 2026-09-29 143413" src="https://github.com/user-attachments/assets/6db93b6d-8fce-46c8-a42d-91b69a4e919f" />

<img width="1858" height="972" alt="Screenshot 2026-09-29 151120" src="https://github.com/user-attachments/assets/05e64bee-6e2a-4ba1-9767-378e7c7b045f" />

<img width="1857" height="967" alt="Screenshot 2026-09-29 143700" src="https://github.com/user-attachments/assets/8f9eac43-2ca7-4539-87b6-1146e23af7ef" />

<img width="1862" height="968" alt="Screenshot 2026-09-29 143714" src="https://github.com/user-attachments/assets/0285bfc2-bead-4f23-ab9a-e92dca6fc341" />

<img width="1855" height="957" alt="Screenshot 2026-09-29 143733" src="https://github.com/user-attachments/assets/b6a9793e-d63a-46da-8da1-a501f0361088" />

<img width="1855" height="972" alt="Screenshot 2026-09-29 143751" src="https://github.com/user-attachments/assets/b277ed3f-3f0b-4aac-b071-05e8865905db" />

<img width="1861" height="966" alt="Screenshot 2026-09-29 143850" src="https://github.com/user-attachments/assets/332a88d4-ba7a-496f-a73a-00b76db963f5" />

<img width="1857" height="966" alt="Screenshot 2026-09-29 143905" src="https://github.com/user-attachments/assets/e513b659-12e9-4189-a7a1-48ff364fbcb8" />

<img width="1861" height="968" alt="Screenshot 2026-09-29 143927" src="https://github.com/user-attachments/assets/dab902d2-a4e9-4a36-9563-f1a9bb561e11" />

<img width="1852" height="965" alt="Screenshot 2026-09-29 143947" src="https://github.com/user-attachments/assets/1cd080f9-8217-4143-b1df-6e79ddcd01ec" />

<img width="1862" height="967" alt="Screenshot 2026-09-29 144511" src="https://github.com/user-attachments/assets/e0914f6a-1359-4b9e-a136-e58a8abc6d0c" />

<img width="1860" height="968" alt="Screenshot 2026-09-29 144534" src="https://github.com/user-attachments/assets/53d617bb-6dbe-4787-9b8d-c281e5a133e4" />

<h2>OUTPUTS :</h2>

<img width="1860" height="967" alt="Screenshot 2026-09-29 152240" src="https://github.com/user-attachments/assets/a31cf65d-f636-4310-88a9-40be5a3c0766" />

<img width="1847" height="938" alt="Screenshot 2026-09-29 152354" src="https://github.com/user-attachments/assets/83784f71-aabe-49c5-89a0-70f6874c809b" />

<img width="1853" height="931" alt="Screenshot 2026-09-29 152447" src="https://github.com/user-attachments/assets/900ae062-6fcd-4dcc-b323-34f0db26a8b3" />

<img width="1847" height="793" alt="Screenshot 2026-09-29 152601" src="https://github.com/user-attachments/assets/ab4f28d6-aabf-4392-9e47-40e432e04fee" />

<img width="1852" height="921" alt="Screenshot 2026-09-29 152637" src="https://github.com/user-attachments/assets/ef92049c-9da6-434b-ac48-d92a3337a51c" />

<img width="1852" height="957" alt="Screenshot 2026-09-29 152724" src="https://github.com/user-attachments/assets/2ac33521-42aa-4d69-a4f0-92b7a891c207" />

<img width="1857" height="967" alt="Screenshot 2026-09-29 152934" src="https://github.com/user-attachments/assets/c3b8e6aa-e876-4250-9ba2-3ffcb631d627" />

<img width="1855" height="967" alt="Screenshot 2026-09-29 153005" src="https://github.com/user-attachments/assets/a61333ae-81a3-4598-9e85-fd5d9b9fc084" />

<img width="1852" height="920" alt="Screenshot 2026-09-29 153031" src="https://github.com/user-attachments/assets/33a9b9dc-f510-4737-83db-61e93c0b91e0" />

<img width="1861" height="966" alt="Screenshot 2026-09-29 153101" src="https://github.com/user-attachments/assets/1b635f85-34b8-4929-a7e6-eee07a225465" />










