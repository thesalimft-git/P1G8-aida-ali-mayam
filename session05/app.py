# # guess number app


# import random

# target = random.randint(1, 100)

# while True:
#     guess = int(input('what is your guess? '))
#     if guess > target:
#         print('go lower')
#     elif guess < target:
#         print('go upper')
#     else:
#         print('you right, answer is: ', target)
#         break
        
        
        


low = 1
hig = 100

print('please select a number between 1, 100')

while True:
    guess = ( low + hig ) // 2
    answer = input(f'is {guess} it ? u/d/c')
    
    if answer == 'u':
        low = guess
    elif answer == 'd':
        hig = guess
    elif answer == 'c':
        print('i win')
        break