print("Please enter valid argument in between 10-18")
a = int(input("Enter Your Age: "))
def voting (a):
    if a in range (10, 17):
        result ="Sorry! You're not eligble for voting."
    elif a in range (18,40):  
        result ="Congrts, You're eligble for voting." 
    else:
        result ='Please enter valid argument 10-20.' 
    return result

print(voting (a))
