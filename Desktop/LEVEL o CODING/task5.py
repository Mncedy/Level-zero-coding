# Area of the Triangle using the sides
def triangleArea():
    s = (x + y + z) / 2 #Calculating semiperimeter
    area = ((s * (s -x) * (s - y) * (s - z)) **0.5) #Herons's formula
    print(area)

x = float(input("Enter a 1st number : "))
y = float(input("Enter a 2nd number : "))
z = float(input("Enter a 3rd number : "))

triangleArea()