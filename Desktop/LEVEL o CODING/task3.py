def boolValue(num1,num2):
    sum = int(num1 + num2)
    val = False
    if sum == 65:
        val = True
    elif num1 == 65 or num2 == 65:
        val = True
    else:
        val
    return val

num1 = int(input("Enter a 1st number : "))
num2 = int(input("Enter a 2nd number : "))
    
print(boolValue(num1,num2))
