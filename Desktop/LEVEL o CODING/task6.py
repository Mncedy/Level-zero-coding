def maxValue(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max


print(maxValue(num1, num2, num3))
