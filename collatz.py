import time, sys

def collatz(number):
    if number % 2 == 0:
        new_number = number // 2
        print(new_number)
        time.sleep(0.3)
        return new_number
    
    else:
        new_number = 3 * number + 1
        print(new_number)
        time.sleep(0.3)
        return new_number
    




def process(d):
    if d == 1: 
        sys.exit()
    else:
        d = collatz(d)
        process(d)

try: 
    user_number = int(input('Please input an integer: '))
    updated = collatz(user_number)
    process(updated)
except ValueError:
    print('Input a non integer string!!!')
    