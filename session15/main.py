from datetime import datetime
from data_manager import set_data, get_data
tasks = get_data()


def show_menu():
    print("\n"*3)
    print("="*50)
    print("1. View")
    print("2. Add task")
    print("3. Mark Done")
    print("4. Delete")
    print("5. Show all")
    print("6. Exit")


def view_task(status='all'):
    if not tasks:
        print('no tasks exist')
    else:
        for id in tasks.keys():
            if 'status' in tasks[id]:
                if status == 'pending':
                    if tasks[id]['status'] == 'pending':
                        print(f"{id}- {tasks[id]['title']}")
                else:
                    print(f"{id}- {tasks[id]['title']}")
            else:
                print('unknown error')
                

def add_task():
    while True:
        title = input('insert task: ')
        if 3 < len(title) < 20 :
            break
        print('title must be in 3 and 20 length')
    
    id = len(tasks) + 1
    now = datetime.now()
    
    tasks[str(id)] = {
        'title': title, 
        'status': 'pending', 
        'time': now.strftime('%Y-%m-%d')
    } 


def edit_task(status):
    view_task('pending')
    while True:
        id = input('which id: ')
        if id in tasks:
            break
        else:
            print('id is not valid')
    
    if tasks[id]['status'] == 'deleted':
        print('id is deleted')
        
    elif tasks[id]['status'] == 'done':
        print('id is already done')
        
    else:  
        tasks[id]['status'] = status
        print(f'task {id} is {status}')


def main():
    while True:
        show_menu()
        command = input('select from menu: ')
        print('='*20)
        print(tasks)
        
        match command:
            case '1':
                view_task('pending')
            case '2':
                add_task()
            case '3':
                edit_task('done')
            case '4':
                edit_task('delete')
            case '5':
                view_task()
            case '6':
                set_data(tasks)
                break
            case _:
                print('is not valid')
                
                
main()




# tasks = {
#     '103': {'title': 'call mom', 'status': 'done', 'time': '2025-04-12'},
#     '104': {'title': 'buy food', 'status': 'pending', 'time': '2025-04-13'}
# }



