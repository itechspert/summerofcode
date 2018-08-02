#Week 1 class 4:

"""
Leap years. Write a program that asks for a starting year and an ending year and
then puts all the leap years between them (and including them, if they are also
leap years). Leap years are years divisible by 4 (like 1984 and 2004). However,
years divisible by 100 are not leap years (such as 1800 and 1900) unless they are
also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!
"""
annual = 0
a = 0

###
x = int(input("Give me a start year: \n > "))
print("You gave me the number: " , str(x))
y = int(input("Give me an end year: \n > "))
print("You gave me the number: ", str(y))
print(x, y)

for a in range(x, y, 4):
    annual = a
    if annual % 400 == 0:
        print(annual)
    elif annual % 100 != 0:
        print(annual)

#And trying it with functions and lists (unsuccessfully, but learned a lot!)

'''
leapyear = []
y = 0
year = 0
def leapyear_find():
    for y in range(0, 3000):
        year = y
        if year % 400 == 0:
            #print(year)
            leapyear.append(int(year))
        elif year % 4 == 0:
            if year % 100 != 0:
                #print(year)
                leapyear.append(int(year))



def leapyear_input():
    x = int(input("Give me a start year: \n > "))
    print("You gave me the number: " , str(x))
    y = int(input("Give me an end year: \n > "))
    print("You gave me the number: ", str(y))
    print(x, y)
    while year in range(x, y):
        print(year)
        if year % 400 == 0:
            print(year)
        elif year % 100 != 0:
            if year % 100 != 0:
                print(year)

leapyear_find()
print(leapyear)
leapyear_input()
leapyear_output()'''

#print("The leap years between " , str(x) , "and ", str(y) , "are " , str(leapyear))

#print(leapyear)
