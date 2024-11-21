# Can one block of except statements handle multiple exception?


try:
    x = 10
    y = int("abc")
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except ValueError as e:
    print(f"Caught a ValueError: {e}")