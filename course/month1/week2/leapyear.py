#Week 1 class 4:

"""
Leap years. Write a program that asks for a starting year and an ending year and
then puts all the leap years between them (and including them, if they are also
leap years). Leap years are years divisible by 4 (like 1984 and 2004). However,
years divisible by 100 are not leap years (such as 1800 and 1900) unless they are
also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!
"""
leapyear = [0, 4]
y = 0

def leapyear_find():
    for y in range(0, 2000):
        year = y
        if year % 400 == 0:
            #print(year)
            leapyear.append(int(year))
        elif year % 4 == 0:
            if year % 100 != 0:
                #print(year)
                leapyear.append(int(year))



def leapyear_print():
    x = int(input("Give me a start year"))
    print("You gave me the number " , str(x))
    y = int(input("Give me an end year"))
    print("You gave me the number ", str(y))

    print(x, y)


leapyear_find()
print(leapyear)
leapyear_print()

#print("The leap years between " , str(x) , "and ", str(y) , "are " , str(leapyear))

#print(leapyear)
'''start_year = ""
end_year = ""
input("Give me a start year")
start_year = input("Give me a start year")
input("Give me an end year")
end_year = input("Give me an end year")

x = input("Give me a start year")
y = input("Give me an end year")
for i in leapyear(x, y)
'''
