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
size = 0

for X in range(0,len(isabel_island)):
    #print (isabel_island[X])
    if X % 2 == 1:
        size = size + 1
    else:
print(size)

#        result = result + isabel_island[i]
#        print (result)
        #print ('my island is ' + result 'in size and is therefore the biggest!')

        #print ("My island is" + result + "and is therefore the biggest island around.")
