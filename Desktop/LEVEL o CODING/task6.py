def max():
    largest = num1

    if (num2 > largest):
        largest = num2
    if (num3 > largest):
        largest = num3
    print(largest)


num1 = int(input("Enter a 1st number : "))
num2 = int(input("Enter a 2nd number : "))
num3 = int(input("Enter a 3rd number : "))

max()