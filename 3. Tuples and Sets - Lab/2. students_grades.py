number_of_students = int(input())

students = {}

for current_student in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for keys, values in students.items():
    grades_list = " ".join(str(f'{value:.2f}') for value in values)
    print(f"{keys} -> {grades_list} (avg: {sum(values)/len(values):.2f})")
