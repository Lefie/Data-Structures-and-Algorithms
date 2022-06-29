# Introduction 

## What is an array?
An array is a data structure that stores values in a contiguous fashion. In other words, items are stored sequentially or one after another in memory.

Note that in python, a list can store items of different data types, whereas an array can only store items of the same data type.

## Why do we use arrays?
We can choose to use an array when 
* we want to store data and iterate over it one by one 
* we want to store multiple values in a single variable 

## Advantages 

* Storing data in sequential order 
* Fast Lookups using index 
* Fast append and pop at the end of the array


## Disadvantages 
* Slow inserts or deletes into/from the middle of the array because the rest of the elements in the array will need to be shifted in order to accomadate the insertion or deletion

* In the case of a static array where the size of the array is fixed, in order to insert a new element that will cause the array to exceed its size, a new array will have to be created. The process of transferring the elements into the new array is O(N)

## Operations
| Operations    | Big O  | Comment  |
| ------------- |:-------------:| :-------------:| 
| lookup        |  O(1)         |     looking up a value using index         |
| append / pop       | O(1)      |    operation is done at the end of the array                |
| insert        | O(n)      | shifting required     |
| delete        | O(n)      | shifitng required    |
| search        |O(n)       | without index, we have to loop through the array to find the item|

## Functions of Python List 
```python
new_arr=[2,3,6,4,5,7]

#access an element in the array O(1)
second_ele=new_arr[1]

#add a new element to the array O(1)
new_arr.append(8)

#remove an element at index 2 
new_arr.pop(1) #O(n) because we deleted it in the middle

#insert an element at position 2 O(N)
new_arr.insert(1,"Alien")

#remove an element with value 7  O(1) or O(N)
new_arr.remove(7)

new_list=new_arr.copy()
new_arr.count("Alien") #returns the number of elements with the value "Alien" in the array
new_arr.extend([2,3,4]) #add a list or any iterable to the end 
new_arr.index("Alien") #return the index of where alien is at 
new_arr.remove("Alien")

new_arr.sort() #sort the array 
new_arr.reverse() #reverse the array 

print(new_arr)

new_arr.clear()

```

## Tips on array
* Be aware of :
    1. An empty sequence 
    2. A sequence with 1 or 2 elements
    3. A sequence with repeated elements
    4. Appearances of duplicates in a sequence
* Arrays and strings are both sequences
