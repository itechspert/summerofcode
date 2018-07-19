#Assign a name to my island, "isabel_island"
#o = sea
#X = land
isabel_island = """ooooooooooo
                   oooXXXooooo
                   ooXXXoooooo
                   ooooXXXXooo
                   ooooXXXXXoo
                   ooXXXXooooo
                   ooooXXXXXoo
                   oooXXXXoooo
                   oooooXXXXoo
                   oooooXooooo
                   ooooooooooo"""

X = 1
o = 0
count = 0

for i in range(len(isabel_island)):
    print (isabel_island[i])
    if X % 2 == 1:
        count =+ 1

print(count)

#        result = result + isabel_island[i]
#        print (result)
        #print ('my island is ' + result 'in size and is therefore the biggest!')

        #print ("My island is" + result + "and is therefore the biggest island around.")
