students = dict()

# students = {
#     '103': {'name': 'ali', 'grades':{}},
#     '104': {'name': 'reza', 'grades':{'chimi': 19}}
# }

def echo_menu():
    print('='*50)
    print("1. Add Student")
    print("2. Assign Grade")
    print("3. Display Student Grades")
    print("4. Exit")

def add_student():
    name = input('student name: ')
    id = len(students) + 1
    students[str(id)] = {'name': name, 'grades': dict()}
    print(f'{name} has added as a student successfully')

def assign_grade():
    show_info_all()
    id = input('which id: ')
    course = input('course: ')
    grade = float(input('grade: '))
    students[id]['grades'][course] = grade
    print(f'{course} with score {grade} is added to student {id}')

def show_info_all():
    for id, student in students.items():
        print(f'{id}- {student.get('name')}')
       
def show_info_student():
    show_info_all()
    id = input('which id: ')
    print(students[id]['name'])
    
    if not students[id]['grades']:
        print('has no score')
    else:
        for course in students[id]['grades']:
            print(f'\t{course} {students[id]['grades'][course]}')
    

def main():
    while True:
        print(students)
        echo_menu()
        command = input('select from menu: ')
        match command:
            case '1':
                add_student()
            case '2':
                assign_grade()
            case '3':
                show_info_student()
            case '4':
                break
            case _:
                print('is invalid, select only from menu')
                
        

main()

