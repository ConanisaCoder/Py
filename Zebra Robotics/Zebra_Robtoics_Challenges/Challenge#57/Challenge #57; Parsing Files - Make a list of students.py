open_file = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge#57/text.txt","r")
readlines = open_file.readlines()
val_dict = {} 
for i in readlines:
    i.replace("\n","")
    student = i[:i.index(" ")].strip()
    student_grade = int(i[i.index(" ")+1:])
    val_dict[student] = student_grade
def Avg_Grade():
    total_len = len(val_dict)
    total_num = 0
    for i in val_dict.values():
        total_num += i
    avg = total_num / total_len
    return avg
def Top_Students():
    list_students = []
    grades = list(val_dict.values())
    grades.sort(reverse=True)
    val = 0
    for i in range(0,3,1):
        grade_index = grades[val]
        for students in val_dict:
            if val_dict[students] == grade_index:
                list_students.append(str(students) + ": " +str(grade_index))
        val += 1
    return list_students
def List_Fail():
    students = val_dict.keys()
    failing_students = ""
    for student in students:
        grade = val_dict[student]
        if grade < 50:
            failing_students += student + " "
    return failing_students
print("1) The Average Grade\n2) Top 3 performing students\n3) List of students Failing\n4) Add student and grade\n5) Update Score\n6) Exit")
input_file = int(input("What would like to Know: "))
match input_file:
    case 1:
        print(Avg_Grade())
    case 2:
        print(Top_Students())
    case 3:
        print(List_Fail())
open_file.close()