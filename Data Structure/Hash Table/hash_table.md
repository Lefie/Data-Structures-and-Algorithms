# Introduction 

## What is a hash table?
A hash table (commonly referred to as a hash map) is a data strcuture which maps keys to values through implementing an associative array. A hash map also uses a hash function to compute an index into an array of buckets or slots, which then produce correct values

* Note that hash maps are usually unordered, but in python, hash map has become ordered.
* A hash map does not allow duplicate keys 
## Why do we use a hash table?
Instead of traversing through the array and searching for the element that we want to find, it is very fast using a hash table to check whether an element exists. 


## Advantages 
* Quick lookup O(1)
* Quick insertion and deletion




## Disadvantages 
* Hash collisions could occur
* More space is needed (Classic example of time and space trade off)


## Operations
| Operations    | Big O  | Comment  |
| ------------- |:-------------:| :-------------:| 
| insert        | O(1)      | Average case     |
| delete        | O(1)      | Average case    |
| search        |O(1)       | Average case |

## Functions of a hash table
```python
#An empty dictionary 
my_dict={}

#an dictionary with items
new_dict={"Apple":2, 
"Lemon":7,
"Pear": 5
}

print(new_dict)

# Lenght of the dictionary 
print(len(new_dict))

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
print(new_dict)

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






```



