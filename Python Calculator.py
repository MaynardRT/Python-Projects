#Basic Mathematical Operation using Python


print ('\nPython Calculator')
print ('\n')
number1 = float(input('Enter the first number: ' ))
number2 = float(input('Enter the second number: ' ))
operation = int(input('Please select the operation to be use: 1. Add, 2. Minus, 3. Multiply, 4. Divide: '))


if (operation == 1):
    answer1 = number1 + number2
    print ("\n The sum of: " + str(number1) + " + " + str(number2) + " = " + str(answer1))
elif (operation == 2):
    answer2 = number1 - number2
    print ("\n The difference of: " + str(number1) + " - " + str(number2) + " = " + str(answer2))
elif (operation == 3):
    answer3 = number1 * number2
    print ("\n The product of: " + str(number1) + " * " + str(number2) + " = " + str(answer3))
elif (operation == 4):
    answer4 = number1 / number2
    remainder = answer4 % 2
    print ("\n The qoutient of: " + str(number1) + " / " + str(number2) + " = " + str(answer4))
    if (remainder != 1):
     print ("\n Remainder" + " " + str(remainder)) 
else:
    print ('Error! Please select the corresponding number for operation.')

print ("\n")
