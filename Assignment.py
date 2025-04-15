
def get_student_data():
    students = []
    num = int(input("Enter number of students: "))
    
    for i in range(num):
        print(f"\nEnter details for Student {i + 1}:")
        name = input("Name: ")
        physics = float(input("Physics Grade: "))
        chemistry = float(input("Chemistry Grade: "))
        biology = float(input("Biology Grade: "))
        math = float(input("Mathematics Grade: "))

        average = (physics + chemistry + biology + math) / 4
        status = "Pass" if average >= 50 else "Fail"
        
        student = {
            "Name": name,
            "Physics": physics,
            "Chemistry": chemistry,
            "Biology": biology,
            "Mathematics": math,
            "Average": average,
            "Status": status
        }
        students.append(student)
    
    return students


def display_results(students):
    print("\nStudent Results:\n")
    for student in students:
        print(f"Name: {student['Name']}")
        print(f"  Physics: {student['Physics']}")
        print(f"  Chemistry: {student['Chemistry']}")
        print(f"  Biology: {student['Biology']}")
        print(f"  Mathematics: {student['Mathematics']}")
        print(f"  Average: {student['Average']:.2f}")
        print(f"  Status: {student['Status']}")
        print("-" * 30)


# Main Program
students = get_student_data()
display_results(students)

