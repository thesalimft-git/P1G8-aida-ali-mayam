import random

while True: 
    pc_choice = random.choice(['r', 'p', 's'])
    h_choice = input('what is your choice r/p/s: ')
    
    if h_choice == 'end':
        break

    elif pc_choice == h_choice :
        print('same choice, try again')
        
    elif pc_choice == 'r':
        if h_choice == 'p':
            print('you win')
        else:
            print('you lost')

    elif pc_choice == 'p':
        if h_choice == 's':
            print('you win')
        else:
            print('you lost')

    elif pc_choice == 's':
        if h_choice == 'r':
            print('you win')
        else:
            print('you lost')
        