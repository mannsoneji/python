# When is the finally block executed?

# the finally block in python execute whether an exception was raised or not in try block 

# it is typically usesd to cleanup all actions 

# example of finally block

def example_finally():
    try:
        x = 10 / 2 
        
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")

    finally:
        print("This will always be executed, no matter what.")

example_finally()