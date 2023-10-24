"""Practice with dictionary syntax"""

# creating a new dictionary
ice_creams: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# adding a key,value pair to a dictionary
ice_creams["mint"] = 3
print(ice_creams)

#removing an element
ice_creams.pop("mint")
print(ice_creams)

#printing out how many orders are there of a specific element and updating the value
print(ice_creams["chocolate"])
ice_creams["chocolate"] += 10
print(ice_creams["chocolate"])


