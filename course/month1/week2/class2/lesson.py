
"""```python
for i in range(65,65+2*26):
    print(i, " stands for ", chr(i))
```"""
#Fix the above so it prints only A-Z and a-z

#Make a function that prints A-Z and a-z
#Make a function that asks the user for a message and turns it into a list of numbersself.
#E.g. "I LOVE YOU" -> [73, , 76, , ...] It's a cypher;))



"""a = "Elle J"
b = "Sarah"
c = "Jeanette"
d = "Melinda Gates"
students = [a, b, c, d]
print(students[0], students[1], students[2])
print("You are now a student next to " + students[1])

sisters = ["Christina", "Jessie RS", "alteredco", "LamboFantastico"]

print(sisters)

members = [students, sisters]
print(members)
print(members[1][3])"""


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
    #To show that we have already counted land we FLAG the land (see below!)
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
