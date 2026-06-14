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
    # '103': {'name': 'ali', 'grades':{}},
    students.update({})

def assign_grade():
    print('assign_grade')

def show_info_all():
    print('show_info_all')

def show_info_student():
    print('show_info_student')

def main():
    while True:
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