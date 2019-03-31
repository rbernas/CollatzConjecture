def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

print('Enter number:')

userNumber = input()

try:
    while int(userNumber) != 1:
        number_local = collatz(int(userNumber))
        print(number_local)
        userNumber = number_local
except ValueError:
    print('Please enter an integer.')
    
