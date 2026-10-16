import csv
import os
FILE_NAME="student_marks.csv"
SUBJECTS=["Python","SQL","Java"]
def load_students():
    students=[]
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r",newline="")as file:
            reader=csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students
def save_students(students):
    fields=["Roll_no","Name"]+SUBJECTS
    with open(FILE_NAME,"w",newline="")as file:
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)
def calculate_result(student):
    marks=[int(student[subject])for subject in SUBJECTS]
    total=sum(marks)
    average=total/len(SUBJECTS)
    if average>=90:
        grade="A"
    elif average>=75:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=40:
        grade="D"
    else:
        grade="F"
    return total,average,grade
def add_students(students):
    roll_no=input("Enter roll number:").strip()
    if any(s["Roll_no"]== roll_no for s in students):
        print("Roll number already exists!")
        return
    name=input("Enter student name:").strip()
    print("Student name Entered:",name)
    if not name:
        print("Name cannot be empty!")
        return
    student={"Roll_no":roll_no,"Name":name}
    for subject in SUBJECTS:
        while True:
            try:
                mark=int(input(f"Enter {subject} marks(0-100):"))
                if 0<= mark <=100:
                    student[subject]=str(mark)
                    break
                else:
                    print("Mark must be between 0 to 100.")
            except ValueError:
                print("Please enter a valid whole number.")
    students.append(student)
    save_students(students)
    print("Student added successfully!")
def display_students(students):
    if not students:
        print("No student records found!")
        return
    print("\n"+"-"*85)
    print(f"{'Roll No':<10}{'Name':<15}{'Python':<10}"f"{'SQL':<10}{'Java':<10}{'Total':<10}"f"{'Average':<10}{'Grade':<8}")
    print("-"*85)
    for student in students:
        total,average,grade=calculate_result(student)
        print(f"{student['Roll_no']:<10}"f"{student['Name']:<15}"f"{student['Python']:<10}"f"{student['SQL']:<10}"f"{student['Java']:<10}"f"{total:<10}"f"{average:<10.2f}"f"{grade:<8}")
    print("-"*85)
def search_student(students):
    roll_no=input("Enter roll number to search:").strip()
    for student in students:
        if student["Roll_no"]==roll_no:
            total,average,grade=calculate_result(student)
            print("\n Student Details")
            print("Roll number:",student["Roll_no"])
            print("Name:",student["Name"])
            for subject in SUBJECTS:
                print(f"{subject} Marks:",student[subject])
            print("Total marks:",total,"/300")
            print(f"Average:{average:.2f}")
            print("Grade:",grade)
            return
    print("Student not found!")
def show_topper(students):
    if not students:
        print("No student records found!")
        return
    topper=max(students,key=lambda student:calculate_result(student)[0])
    total,average,grade=calculate_result(topper)
    print("\n Class Topper")
    print("Roll number:",topper["Roll_no"])
    print("Name:",topper["Name"])
    print("Total marks:",total,"/300")
    print(f"Average:{average:.2f}")
    print("Grade:",grade)       
def main():
    students=load_students()
    while True:
        print("\n========STUDENT MARK MANAGEMENT SYSTEM =========")
        print("1.Add student")
        print("2.Display all students")
        print("3.Search student")
        print("4.Show class topper")
        print("5.Exit")
        choice=input("Enter your choice (1-5):").strip()
        if choice =="1":
            add_students(students)
        elif choice =="2":
            display_students(students)
        elif choice =="3":
            search_student(students)
        elif choice=="4":
            show_topper(students)
        elif choice=="5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Pleease enter 1-5.")
if __name__=="__main__":
    main()
        























