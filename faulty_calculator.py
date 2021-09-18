'''
Exercise : Faulty Calculator
WAP a calculator which will correctly solve all the problem except
the following ones:
356 * 353 = 34567, 3456 + 98765 = 1234567654, 5567 / 7656 = 44376
Program should take operator and two numbers as inputs and the return
the result
'''

print("CALCULATOR\n")

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))

print("\n=====Choose operators=====")

print("\n\tOperator sign: '+' for Addition."
      "\n\tOperator sign: '-' for Subtraction"
      "\n\tOperator sign: '*' for Multiplication"
      "\n\tOperator sign: '/' for Division")

oper = input("\nEnter the operator sign: ")

if oper == '+':
      if num1 == 3456 and num2 == 98765:
            print("Sum of number is 1234567654")
      else:
            print("Sum of numbers is", num1 + num2)


if oper == '-':
      print("Subtraction of "+ str(num2)+ ' from ' + str(num1) + " is", num1 - num2)


if oper == '*':
      if num1 == 356 and num2 == 353:
            print("Multiplication of " + str(num1) + " and " + str(num2) + " is: 34567")
      else:
            print("Multiplication of " + str(num1) + " and " + str(num2) + " is: ",num1*num2)

if oper == '/':
      if num1 == 5567 and num2 == 7656:
            print("Division of " + str(num1) + " and " + str(num2) + " is: 44376")
      else:
            print("Division of " + str(num1) + " and " + str(num2) + " is: ", num1/num2)


print("\n\n\t\t\t----------THANK YOU----------")



