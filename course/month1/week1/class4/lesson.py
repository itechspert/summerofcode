'''i = 1
while i < 11:
    print(i)
    i = i + 1

j = 0
while j < 11:
    print(j)
    if j == 3:
        break
    j += 1
'''
text = ""

'''while text != "bye":
    text = input("say something please ")
    print ("you said " + text + ".")

    if text == "bye":
        print ("good bye to you too")
        break
'''

'''
while text != "bye":
    text = input("say something please : ")

    if text != "bye":
        print ("you said " + text + ".")

    if text == "bye":
        print ("good bye to you too")
'''

'''for x in range(5, 50, 3):
    print(x)
'''
'''
students = ("Baby girl", "Bella12", "Kat Butler", "Issy Airas", "Saakshi Bansal", "Livia")
for s in students:
  if len(s) > 7:
      print (s + " is an amazing Pythonista and has a very long name")
      if len(s) == 9:
        print("Supercalifragilisticexpialidocious")
  elif len(s) == 7:
        print (s + " is an amazing Pythonista and has a name that's exactly 7 characters long!")
  elif len(s) < 13:
        print (s + " is an amazing idiot")
  else:
    print (s + " is an amazing Pythonista and a minimalist!")
'''

students = ["Baby girl", "Bella12", "Kat Butler", "Issy Airas", "Saakshi Bansal", "Livia"]
'''for s in students:
    print(s)

list comprehension
usernames = [doseomthing(element) for everyelement in list]

usernames = [s + "@1mwtt" for s in students]
print(usernames)
'''
'''usernames = [s + "@1mwtt" for s in students]
print (usernames)

students.append("Marta Bodojra")
print(students)
students.pop()
print(students)
students.sort()
print(students)
'''
#SOLVED ILONA'S PROBLEM WITH SORTING!
'''fruits = ["orange", "banana", "apple", "kiwi"]
print(fruits)
fruits.sort()
print(fruits)
'''
