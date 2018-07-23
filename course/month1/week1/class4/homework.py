# “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
'''bottles = 99
for b in str(bottles):
    song = "I've got ", str(bottles), " bottles of beer on the wall, ", str(bottles), "bottles of beer. Take one down and pass it around, ", str(bottles - 1), " bottles of beer on the wall."
    print(song)
    bottles = bottles - 1
''''''
while bottles >= 0:
    song = "I've got ", str(bottles), "bottles of beer on the wall, ", str(bottles), "bottles of beer. Take one down and pass it around, ", str(bottles - 1), "bottles of beer on the wall."
    print(song)
    bottles = bottles - 1
'''
'''import random
text = ""

while text != ("bye"):
    text = input("HUH?! SPEAK UP GIRL ")

    if str.isupper(text):
        year = random.randint(1930, 1950)
        print("NO, NOT SINCE", year, ""''')


'''while text != "bye":
    text = input("say something please ")
    print ("you said " + text + ".")

    if text == "bye":
        print ("good bye to you too")
        break
'''


'''Leap years. Write a program that asks for a starting year
and an ending year and then puts all the leap years between them
(and including them, if they are also leap years). Leap years are
years divisible by 4 (like 1984 and 2004). However, years divisible
by 100 are not leap years (such as 1800 and 1900) unless they are
also divisible by 400 (such as 1600 and 2000, which were in fact
leap years). What a mess!'''

leapyear = 0
     
