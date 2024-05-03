print("Please enter valid argument in between 10-18")
a = int(input("Enter Your Age: "))
def voting (a):
    if a in (10, 11, 12, 13, 14, 15, 16, 17):
        result ="Sorry! You're not eligble for voting."
    elif a in (18, 19, 20):  
        result ="Congrts, You're eligble for voting." 
    else:
        result ='Please enter valid argument 10-20.' 
    return result

print(voting (a))
