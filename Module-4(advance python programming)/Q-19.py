# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.


# try block : that may raise exceptions 
# except : specify how to handle that exceptions
# finally : ensure that certain code runs whether an exception occurs


def divide(a,b):
    try:
        result = a / b
        print(result)

    except ZeroDivisionError as e:
        print("Error",e)
    
    finally:
        print("This will always execute")


divide(10,0)