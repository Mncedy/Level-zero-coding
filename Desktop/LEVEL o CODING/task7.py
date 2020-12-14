def fahrenheit(c):
    return ((c * 9/5) + 32)

def celsius(f):
    return ((f - 32) * 5/9)

val = 0
while val == 0:
    print("Enter 1 to convert Celsius into Fahrenheit")
    print("Enter 2 to convert into Fahrenheit into Celsius")
    types = int(input("Enter your choice : "))

    if types == 1:
        c = float(input("Enter Degrees Celsius temperature : "))
        print("Fahrenheit temperature is: ", fahrenheit(c))
        break
    if types == 2:
        f= float(input("Enter Degrees Fahrenheit temperature : "))
        print("Celsius temperature is: ", celsius(f))
        break
    if types != 1 or types !=2:
        val = 1
        print("Invalid number, please enter 1 or 2")
        