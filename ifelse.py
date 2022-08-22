'''
take 2 numbers if 1st number is greather than 2nd number print
'''

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))

if a<b:
    print(f"{a}is greater than {b}")
elif a>b:
    print(f"{a} is lesser than {b}")
else:
    print(f"{a} is equal to {b}")

