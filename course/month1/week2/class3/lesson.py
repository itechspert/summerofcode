'''#dictionary constructor:
isabel_airas = dict(name = "Isabel Airas", discord_id = "issytechspert", fav_food = "sushi")

print(isabel_airas)

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}
print(my_dict)

#Dictionary is an unordered collection and you cannot have repetitions, wheras with lists you can.

# access
print(my_dict["a"])

# add
my_dict["Rocio"] = "pretty"
print(my_dict["Rocio"])
print(my_dict)

# modifying
my_dict["a"] = 50
print(my_dict["a"])
print(my_dict)
#delete an items
del(my_dict["a"])
print(my_dict)
print(len(my_dict))
#delete Dictionary
del(my_dict)
print(my_dict)

#There are two ways of creating - **instantiating** a dictionary:
- notation {}
- constructor functions
notation
my_var ={}

Constructor:
my_var = dict()

Classes

class Student():
    def __init__(self, name, discord_id, fav_food, dream):
        self.name = name
        self.discord_id = discord_id
        self.fav_food = fav_food
        self.dream = dream

    def my_print(self):
        print(self.name + ", " + self.discord_id + ", " + self.fav_food + ", " + self.dream)

#self is something to show Python that you're creating an object. self. is the first variable /parameter needs to be first.
#instantiate (creation of an actual student) using our shiny new constructor function thta we got for 'free' from the class

s1 = Student("Virginia Balseiro", "virginia [Gold] [volunteer]", "pizza", "moving to Sweden")
s2 = Student("issytechspert")
s3 = Student("isabel_airas[VIP]")


print(s1)
print(s1.fav_food)
print(s1.discord_id)
s1.my_print()
s1.fav_food = "ice-cream"
s1.my_print()
del s1.fav_food
s1.my_print()

#dot-notation helps it read which class it is.

del s1
print(s1)
s1.my_print()'''
