"""def moo(n):
#    print('moo' * n)
    return 'moo' * n

moo(0)
moo(1)
moo(2)
"""

#for i in range(3):
#    moo(i)

#Homework: Write unittests for previous functions that I have created in Learn to Python the Hard Way
def ask_recursively(question):
    print(question)
    reply = input('> ').lower()
    if reply == 'yes':
        return True
    if reply == 'no':
        return False
    else:
        print('Please answer "yes" or "no"')
        ask_recursively(question)

ask_recursively('Do you wet the bed?')

'''
#Reading and writing files
filename = "alice_in_wonderland.txt"
file = open(filename, "r")
for line in file:
    print(line)

raw = file.read()
print('from zero to sixty-five' + raw[:65])

print('from zero to sixty-five' + raw[0:65])
print('from sixty-five to six-hundreet' + raw[65:600])

print('the length of Alice in Wonderland in this text file is:' + str(len(raw)))

print(raw[163000:])

#TO DO:'''
# Calculate a table for each letter in the alphabet from a-z, and count how many
#times each letter appears in Alice in Wonderland.
# (Fancy word for counting stuff is "frequency distribution" because you're counting frequency)
#: a: 3200
# b: 3839
