# Password Strength Checker

a = input("Enter your password: ")

up = 0   # uppercase
sm = 0   # lowercase
di = 0   # digits
sp = 0   # special characters

if len(a) > 7:
    for i in a:
        if i.isupper():
            up += 1
        elif i.islower():
            sm += 1
        elif i.isdigit():
            di += 1
        else:
            sp += 1

    if (up > 0 and sm > 0 and di > 0 and sp > 0):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Less Characters (Minimum 8 required)")
