"""Instantiating a Class"""

"""
This is where we instantiate the class we defined in classes.py.
In other words, we're creating objects that belong to that class.
"""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # empty constructor. This allows us to construct a new pizza


# access/set/update attribute values
my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True



# check the values of specfic attributes
print("Size: ")
print(my_pizza.size)

print("my_pizza:")
print(my_pizza) # prints the object reference

# Make sals_pizza size medium, 5 toppings, Not gluten free

sals_pizza: Pizza = Pizza("medium", 5, True)
print(sals_pizza.size)


# this is  function and NOT a method
def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75(input_pizza.toppings)
    if input_pizza.gluten_free:
        cost += 100
    return cost

# calling a method

print(sals_pizza.price())


