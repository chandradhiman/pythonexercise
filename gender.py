def greet(gender=None):
    if gender in ("male", "m", "mlae", "mle"):
        greet = "Hello Sir"
    elif gender in ("female", "f"):
        greet = "Hello Ma'am"
    else:
        greet = "Hello"
    
    return greet

a = str(input("Enter Gender: "))

hello = greet(a)
print (hello)
