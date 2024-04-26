

##calcultor by python.

"""""print(15//6)
print(5%3)
porint(5**3)## 5*3, 2 times
"""""

def arthematic(a, b, x=None):
    print(a, " ", type(a)) 
    print(b, " ", type(b))
    if x=='add':
        value =a+b
    elif x == 'sub':
        value = a-b
    elif x == 'multiplication':
        value = a*b
    elif x == 'divide':
        value = a/b
        return 'invalid operator'
    return value
print("use add(+) , sub(-), mul(*), divide(/)")
a = float(input("Enter a number: ")) 
b =int(input("Enter b number: "))
x =str(input("Enter x string: "))
print (arthematic(a, b, x))

