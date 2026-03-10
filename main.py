def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

students = []

num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    print("\nStudent", i + 1)
    name = input("Enter the student's name: ")
    num_subjects = int(input("Enter the number of subjects: "))
    marks = []
    for j in range(num_subjects):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)
    avg = sum(marks) / num_subjects
    grade = calculate_grade(avg)
    
    if avg >= 50:
        status = "Pass"
    else:
        status = "Fail"
    
    student = {"name": name, "average": avg, "grade": grade, "status": status}
    students.append(student)

print("\nStudent Results:")
for student in students:
    print(f"{student['name']} | Average : {student['average']:.2f} | Grade = {student['grade']} | Status = {student['status']}")