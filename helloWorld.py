def greeting(name):
    print 'Hello %s' %name

def addnum(n1,n2):
    return n1 + n2

def ageCheck(age):
    if age <= 12:
        print "Damn you're a kid"
    elif age > 12 and age < 21:
        print "No booze for you"
    else:
        print "%s you're good to go. Let's get wasted!" %name
    
name = raw_input("Enter your name -> ")
greeting(name)
number1 = int(input("Think of a number -> "))
number2 = int(input("Think of another number -> "))
print "Tada, those two numbers add up to ->", addnum(number1,number2)
print "Now we've got that out of the way, how old are you? -> "
age = int(input())
ageCheck(age)
