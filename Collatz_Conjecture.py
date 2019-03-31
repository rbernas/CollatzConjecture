def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

print('Enter a positive integer:')
userNumber = input()
    

try:
    while int(userNumber) != 1 and int(userNumber) > 0:
        number_local = collatz(int(userNumber))
        print(number_local)
        userNumber = number_local
    else:
        print('Please enter a positive integer.')
except ValueError:
    print('Please enter a positive integer.')
    
