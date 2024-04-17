# Project '3' : Calculator App

print('Welcome to the calculator app...')

try:
    chooses = input('Enter the given operator (+,-,*,/):\n')


    if chooses in ('+','-','*','/'):
    
        num1 = int(input('Enter the first number:\n'))
        num2 = int(input('Enter the second number:\n'))
    
        if chooses == '+':
            result = num1 + num2
            print('The sum of two numbers is: {}'.format(result))
        
        elif chooses == '-':
            result = num1 - num2
            print('The difference of two numbers is: {}'.format(result))

        elif chooses == '*':
            result = num1 * num2
            print('The multiplication of two numbers is:{}'.format(result))

        elif chooses == '/':
            result = num1 / num2
            print('The division of two numbers is:{}'.format(result))

    else:
        print('Invalid operator.....')
except ZeroDivisionError:
    print ('Zero cannot be divided to any number')

except ValueError:
    print('String cannot be used only integer is used.')


except TypeError:
    print('it is not happening..')
