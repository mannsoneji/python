try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))

    ans = a * b

    print(ans)

except:
    print("Invlid input")
else:
    print("ans = ",ans)

finally:
    print("THANKYOU FOR USING THIS APPLICATION ")