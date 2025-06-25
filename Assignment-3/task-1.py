def fact1(a):
    if a <= 1:
        return 1
    else:
        return a*fact1(a-1)
num = int(input("Enter a number: "))
factorial = fact1(num)
print(f"Factorial of {num} is {factorial}")
