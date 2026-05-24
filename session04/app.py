#  variable, loop, condition, function

# print, len, input, range
# define, call
# def is_even(x: int) -> bool:
#     return x % 2 == 0

# is_even(102)
# is_even(103)


def is_prime(x:int):
    x_is_prime = True
    for i in range(2, x):
        if x % i == 0:
            x_is_prime = False
        
    if x_is_prime:
        print('it is prime')
    else:
        print('it is not')
    

print(is_prime(610875316508723610439641030))
# print(is_prime(73))
# print(is_prime(75))