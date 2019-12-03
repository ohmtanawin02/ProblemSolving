number = int(input('Enter number : '))
integer = number
number1 = 1
number2 = 1
count = 0
if integer <= 0:
    print("Please enter positive integer")
elif integer == 1:
    print("Fibonacci sequence",integer,":")
    print(number1)
else:
    print("Fibonacci sequence",integer,":")
    while count < integer:
        print(number1,end=' ')
        numbertotal = number1 + number2
        number1 = number2
        number2 = numbertotal
        count +=1