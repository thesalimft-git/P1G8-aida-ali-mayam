import random

pc_win = 0
h_win = 0

while True: 
    pc_choice = random.choice(['r', 'p', 's'])
    h_choice = input('what is your choice r/p/s: ')
    
    if h_choice == 'end':
        print(f'pc: {pc_win}, you: {h_win}')
        break

    elif pc_choice == h_choice :
        print('same choice, try again')
        
    elif pc_choice == 'r':
        if h_choice == 'p':
            h_win += 1
            print('you win')
        else:
            pc_win += 1
            print('you lost')

    elif pc_choice == 'p':
        if h_choice == 's':
            h_win += 1
            print('you win')
        else:
            pc_win += 1
            print('you lost')

    elif pc_choice == 's':
        if h_choice == 'r':
            h_win += 1
            print('you win')
        else:
            pc_win += 1
            print('you lost')
        