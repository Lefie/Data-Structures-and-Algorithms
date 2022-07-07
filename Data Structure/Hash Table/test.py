new_dict={"Apple":2, 
"Lemon":7,
"Pear": 5
}




#Accessing items
x = new_dict["Lemon"]
print(x)

print(new_dict.get("Lemon"))

#Get keys
x = new_dict.keys()
print(x)

#Get values
x = new_dict.values()
print(x)

#Get items
x = new_dict.items()
print(x)

#Change items
new_dict["Lemon"] = 5
new_dict.update({"Pear":10})


#Add items 
new_dict["Orange"]=17
print(new_dict)

#Remove items
new_dict.pop("Orange")
# new_dict.popitem() (remove the last item)
del new_dict["Lemon"]
print(new_dict)

#del new_dict (delete the whole dictionary )
#new_dict.clear() (cleans the dictionary )

# Looping through keys in a dictionary 
for x in new_dict:
    print(x)

for x in new_dict.keys():
    print(x)
# Looping through values in a dictionary 
for x in new_dict:
    print(new_dict[x])

for x in new_dict.values():
    print(x)

# looping through items
for x,y in new_dict.items():
    print(x,y)

# copy a dictionary 
newer_dict =new_dict.copy()