# Introduction 

## What is an array?
An array is a data structure that stores values in a contiguous fashion. In other words, items are stored sequentially or one after another in memory. In python, an array is called a list.

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
| lookup        |  O(1)         |                |
| append / pop       | O(1)      |    operation is done at the end of the array                |
| insert        | O(n)      | shifting required     |
| delete        | O(n)      | shifitng required