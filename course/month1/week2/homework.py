#Week 1 class 4:
'''
Leap years. Write a program that asks for a starting year and an ending year and
then puts all the leap years between them (and including them, if they are also
leap years). Leap years are years divisible by 4 (like 1984 and 2004). However,
years divisible by 100 are not leap years (such as 1800 and 1900) unless they are
also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

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

start_year = ""
end_year = ""
input("Give me a start year")
start_year = input("Give me a start year")
input("Give me an end year")
end_year = input("Give me an end year")

x = input("Give me a start year")
y = input("Give me an end year")
for i in leapyear(x, y)

- Building and sorting an array. Write the program that asks us to type as many
words as we want (one word per line, continuing until we just press Enter on an
empty line) and then repeats the words back to us in alphabetical order. Make
sure to test your program thoroughly; for example, does hitting Enter on an
empty line always exit your program? Even on the first line? And the second?

'''
def word_function():
    words = []
    while 0 == 0:
        new_word = input("What word would you like to add to my list?")
        if new_word == "":
            break
        elif new_word != "":
            words.append(new_word)
            print(words)
    print(sorted(words))

word_function()

'''
- Table of contents. Write a table of contents program here. Start the program
with a list holding all of the information for your table of contents (chapter
names, page numbers, and so on). Then print out the information from the list
in a beautifully formatted table of contents. Use string formatting such as
left align, right align, center.'''
''''
table = [["chapter 1", "chapter 2", "chapter 3", "chapter 4", "chapter 5"],
["Introduction", "Living happily", "Testing limits", "Writing stories", "Concluding remarks"],
["1-7", "7-12", "12-22", "22-26", "27-40"]]
print(table[1])

'''
### Writing Your Own Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

```python
def say_moo():
  print("moo")

# let's call it
say_moo()

#### Function Parameters

Information can be passed to functions as parameter.

Parameters are specified after the function name, inside the parentheses.
 You can add as many parameters as you want, just separate them with a comma.

python
def praise(student):
    print(student + " is an amazing Pythonista!")

praise("Katie")

The following example shows how to use a default parameter value.

If we call the function without parameter, it uses the default value:

```python
def praise(student = "Melinda"):
    print(student + " is an amazing Pythonista!")

praise()

Melinda is an amazing Pythonista!
```

#### Thing to Try

Write a function that prints out "moo" n times.
'''
'''
#### Return Values
You may have noticed that some methods give you something back when you call
them. For example, we say gets returns a string (the string you typed in),
and the + method in 5+3 (which is really 5.+(3)) returns 8. The arithmetic
methods for numbers return numbers, and the arithmetic methods for strings
return strings. It’s important to understand the difference between a method
returning a value (returning it to the code that called the method), and your
program outputting information to your screen, like print() does, which we call
a **side-effect**. Notice that 5+3 returns 8; it does not output 8 (that is,
display 8 on your screen).

So, what does print() return? We never cared before, but let’s look at it now:

```
a = print('b')
print(a)

None
```

The first print() didn’t seem to return anything, and in a way it didn’t; it returned `None`. Though we didn’t test it, the second print() did, too; print() always returns None. Every method has to return something, even if it’s just the special value `None`.

Take a quick break, and write a program to find out what say_moo returns.



#### A Few Things to Try

- Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.

No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.

Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.

Hint: Use the integer division and modulus methods.

For reference, these are the values of the letters used:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

- “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
'''
'''

## Helpful links

Problem solving

- Video: https://www.coursera.org/lecture/duke-programming-web/a-seven-step-approach-to-solving-programming-problems-AEy5M
- Book: The Algorithm Design Manual by Steven S Skiena
- Cheat Sheet: http://adhilton.pratt.duke.edu/sites/adhilton.pratt.duke.edu/files/u37/iticse-7steps.pdf

GitHub

- *THE* Git book: https://git-scm.com/book/en/v2 """

"""
Week 2 class 1:
Homework: Write unittests for previous functions that I have created in Learn to Python the Hard Way
file: week2/class1/lecturenotes.py
Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in Alice in Wonderland.
(Fancy word for counting stuff is "frequency distribution" because you're counting frequency)
: a: 3200
 b: 3839"""

 #Week 2 Homework
 #Python the hard way read 10 exercises and do 1 per day
#Week 2 Class 2
"""
```python
for i in range(65,65+2*26):
    print(i, " stands for ", chr(i))
```
#Fix the above so it prints only A-Z and a-z

"""
Make a function that prints A-Z and a-z
Make a function that asks the user for a message and turns it into a list of numbersself.
E.g. "I LOVE YOU" -> [73, , 76, , ...] It's a cypher;))


Optional: Write a function that does a ceaser cycpher (Google), ask the user a number, and shift their message by that number. '''


#Continent counter from 49:00 onward in the week2class2 video


"""Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. Each line should be read from beginning to end.
Now write a function that prints out all elements in reverse.


M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]

def continent_counter(world, x, y):
    if world[y][x] != 'land':
        return 0

    size = 1
    world[y][x] = 'counted land'
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    # row above
    size = size + continent_counter(world, x-1, y-1)
    #print('first recursion size: ' , size)
    size = size + continent_counter(world, x  , y-1)
    size = size + continent_counter(world, x+1, y-1)

    # same row
    size = size + continent_counter(world, x-1, y  )
    size = size + continent_counter(world, x+1, y  )

    # row below
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x  , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size

print(continent_counter(world, 5, 5))


#### Things to try

- There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)

- Write a function that generates an n x n sized board with either land or water chosen randomly.


#### Optional, Advanced

- Run your continent counter for a 20 x 20 board. How long does it take to run? (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT) - make sure you know how to break a running program as it may take a long time to complete and you might not have time to wait for it ;)

- Write test coverage in unittest and/or trace for Continent Counter."""

#Week 2 lecture 3
""" In dictionary:

#### Things to try

- Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

- Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

- Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with `quirky fact`, `fav quote`, `pet`. Practice adding, modifying, accesing.

#### Optional / Advanced

Do Python the Hard Way ex. 39 exercises:

- Mapping with cities and states/regions in your country or some other country.
- Find the Python documentation for dictionaries and try to do even more things to them.
- Find out what you can't do with dictionaries. A big one is that they do not have order, so try playing with that.

Testing

- Write a test to check the outcome of the alice_in_wonderfland task: one test for list of lists, and one test for dictionary output.


```python
frequency_distribution = [
    ["a", 35000],
    ["b", 8000],
    ...
    ["z", 450]
]
``` """'''
#### Things to try

Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.
E.g. create a list that has different options that you give an error if people don't do itself.
Create upgrades and downgrades and subscriptions with methods and functions and print statements to communicate with variables.
Things may be stuff like: self, firstname, lastname, email, country_code, phone_number, github, country, discord_id, fav_food, dream):

Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator to find the meaningful description of reality and translate it for computers.

#### Optional, Advanced

- Come up with a whole taxonomy of Classes for 1MWTT
    - Person()
        - Student()
        - Mentor()
        - Volunteer()
        - Employer()
    Feel free to suggest/invent and also use mixins, decorators, and any other design patterns that you see would help reach the mission of 1 million women to tech by 2020.


Python the Hard Way ex 30 Study Drills

- Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.
- Put the lyrics in a separate variable, then pass that variable to the class to use instead.
- See if you can hack on this and make it do more things. Don't worry if you have no idea how, just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.
- Search online for "object-oriented programming" and try to overflow your brain with what you read. Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me too.

Def:
'''
