number1 = float(input ("Enter the first Number: "))
number2 = float(input ("Enter the second Number: "))
operator = input("Enter an operator (+,-,/,*):  ")

if operator == '+' :
    outcome = number1 + number2
    print ((f"The sum of {number1} and {number2} is :  {outcome}"))
elif operator == '-' :
    outcome = number1 - number2
    print ((f"The difference of {number1} and {number2} is :  {outcome}"))
elif operator == '*' :
    outcome = number1 * number2
    print ((f"The product of  {number1} and {number2} is :  {outcome}"))
else:
    operator == '/'
    outcome = number1 / number2
    print ((f"The quotient of {number1} and {number2} is :  {outcome}"))
    

    









     