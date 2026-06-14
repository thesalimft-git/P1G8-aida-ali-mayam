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
    while True:
        name = input('student name: ')
        if len(name) < 2 or len(name) > 20:
            print('name is not valid, only 3 to 20 characters')
            continue
        elif (not name.isalpha()):
            print('name can be only english letter')
            continue
        else:
            break

    name = name.lower()
    id = len(students) + 1
    students[str(id)] = {'name': name, 'grades': dict()}
    print(f'{name} has added as a student successfully')

def assign_grade():
    show_info_all()
    while True:
        id = input('which id: ')
        if id in students:
            break
        print('id is not valid')


    while True:
        course = input('course: ')
        if len(course) < 2 or len(course) > 20:
            print('course name is not valid')
        else:
            break
    
    
    while True:
        try:
            grade = float(input('grade: '))
            if grade < 0 or grade > 20:
                print('grade can be only between 0 to 20')
                continue
        except:
            print('score must be a number')
            continue
        else:
            break
        
            
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

