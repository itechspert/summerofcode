#Assign a name to my island, "isabel_island"
#o = sea
#X = land
#I want to work out what

o = 0
X = 1
island_evaluator = ""
count = 0

isabel_island = """
ooooooooooo
oooXXXooooo
ooXXXoooooo
ooooXXXXooo
oooooXooooo
ooooXXXXXoo
ooXXXXooooo
ooooXXXXXoo
oooXXXXoooo
oooooXXXXoo
ooooooooooo"""

#print (len(isabel_island))
#length_isabel_island = len(isabel_island)
#print(length_isabel_island)
#How do I check whether a specific letter in a string is there?
for i in range(len(isabel_island)):
    #print(isabel_island[i])
    #if X % 2 == 1:
        #print(isabel_island[i])
#    if "X":
#The island_evaluator is the thing that prints whether it's X or o.
    island_evaluator = isabel_island[i]
#    o = False
#    X = True
    if island_evaluator == "X":
        #print("Yes")
        count += 1
#    print('result just changed to: ' + island_evaluator)
    #    print(isabel_island[i])
print('result : ' + str(count))

#        result = result + isabel_island[i]
#        print (result)
        #print ('my island is ' + result 'in size and is therefore the biggest!')

        #print ("My island is" + result + "and is therefore the biggest island around.")
