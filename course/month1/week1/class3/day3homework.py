#day3 homework

'''Full name greeting. Write a program that asks for a person’s first name, then
 middle, and then last. Finally, it should greet the person using their full name.

Bigger, better favorite number. Write a program that asks for a person’s favorite
 number. Have your program add 1 to the number, and then suggest the result as a
 bigger and better favorite number. (Do be tactful about it, though.)
'''
'''#Naming program
firstname = input("Hi there, what's your name? ")
middlename = input("Hello, " + firstname + " what's your middle name? ")
lastname = input ("Ah excellent, so that\'s " + firstname + " " + middlename + ", what might your surname be then? ")

print ("Brilliant! Welcome, and lovely to meet you, " + firstname + " " + middlename + " " + lastname + "!")
'''
'''
favourite_number = input("Hey there, what's your favourite number? ")
better_number = int(favourite_number) + 1
print("Lol, " + favourite_number + " is shit, my favourite number is " + str(better_number) + "!")
'''
def testfunction():
    want = input("What do you actually want in your life?")
    if want == "to leave":
        print ("Well just go then!")
    else:
        print("WHADDAYA MEAN, \" " + want + "\"?! YOU\'RE TOTALLY FIRED")

testfunction()
