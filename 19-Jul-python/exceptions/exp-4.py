try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))

    ans = a / b

    print(ans)

except ValueError:
    print("Invlid input")
except ZeroDivisionError:
    print("cannot devided by zero")