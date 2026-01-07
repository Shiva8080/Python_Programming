try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")