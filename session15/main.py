from datetime import datetime



tasks = dict()

def show_menu():
    print("\n"*3)
    print("="*50)
    print("1. View")
    print("2. Add task")
    print("3. Mark Done")
    print("4. Delete")
    print("5. Show all")
    print("6. Exit")


def view_pending_task():
    print('view_pending_task')

def add_task():
    title = input('insert task: ')
    id = len(tasks) + 1
    now = datetime.now()
    
    tasks[str(id)] = {
        'title': title, 
        'status': 'pending', 
        'time': now
    } 




def done_task():
    print('done_task')

def delete_task():
    print('delete_task')

def view_all_task():
    print('view_all_task')




def main():
    while True:
        show_menu()
        command = input('select from menu: ')
        print('='*20)
        print(tasks)
        
        match command:
            case '1':
                view_pending_task()
            case '2':
                add_task()
            case '3':
                done_task()
            case '4':
                delete_task()
            case '5':
                view_all_task()
            case '6':
                break
            case _:
                print('is not valid')



main()




# tasks = {
#     '103': {'title': 'call mom', 'status': 'done', 'time': '2025-04-12'},
#     '104': {'title': 'buy food', 'status': 'pending', 'time': '2025-04-13'}
# }

