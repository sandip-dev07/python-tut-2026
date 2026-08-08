# dictionary: collection of unordered unique key-value pairs
# dictionary is mutable
# dictionary is iterable

data = { # key: value pair
        
    22: "Raju",
    56: "Reddy",
    46: "Sandip",
    22: "John" # key represents here as set (unique), so it will override the previous value
}

print(data)
print(data[46]) # Sandip
print(data.get(22)) # Raju
print(data.get(10, "not found")) # not found - default value


keys = {"Raju", "Reddy", "Sandip"}
values = [22, 26, 26]

dict1 = zip(keys, values) # zip object:? {('Raju', 22), ('Reddy', 26), ('Sandip', 26)}
dict1 = dict(dict1)
print(dict1) # {'Raju': 22, 'Reddy': 26, 'Sandip': 26}

# dictionary methods:
print(data.keys()) # dict_keys([22, 56, 46])
print(data.values()) # dict_values(['Raju', 'Reddy', 'Sandip'])
print(data.items()) # dict_items([(22, 'Raju'), (56, 'Reddy'), (46, 'Sandip')])
data.pop(22) # removes the key-value pair

print(22 in data) # True
print(22 not in data) # False