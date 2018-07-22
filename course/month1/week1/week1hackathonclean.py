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

for i in range(len(isabel_island)):
    island_evaluator = isabel_island[i]
#The island_evaluator is the thing that prints whether it's X or o.
    if island_evaluator == "X":
        count += 1
print ("The continent you are standing on is " + str(count) + " units squared and is therefore the biggest island around.")
