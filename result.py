def school (result =None):
    if result in (0-30, "10%", "20%", "30%"):
        school = "Sorry! the result is failed"
    elif result in ("40%", "50%", "60%"):
        school ="Congrts You passed with C grade."
    elif result in ("60%", "70%", "80%"):
        school ="Congrts You passed with B grade."
    elif result in ("80%", "90%", "100%"):
        school ="Congrts You passed with A grade."
    else:
        result ="Hello student"    

    return school
print("Please enter valid argument in between 10%-100%")
a = str(input("Enter Your Marks: "))

hello = school(a)
print (hello)
