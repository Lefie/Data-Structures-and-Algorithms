class Array:
    def __init__(self): #when we initialize a list, the list is initialized to have a length of 0 and a container to store data.
        self.length=0
        self.data=[]
    
    def getVal(self,index): #get value at a certain index 
        return self.data[index]
    
    def push(self,item): #append an item to the end of the list 
        self.data.append(item)
        self.length += 1
        return item 
    
    def getLen(self): # get the length of the list 
        return self.length
    
    def pop(self): #remove the last item of the list and return the item that is going to be removed 
        last_item=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return last_item
    
    def delete(self,index): #delete an item based on the index 
        item_to_delete=self.data[index]
        self.shiftItems(index)

        return item_to_delete
    
    def shiftItems(self,index): #an auxiliary function which shifts all items from the index of the deleted value to the second to the last item one spot to the left
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        
        del self.data[self.length-1] #delete the last location 
        self.length-=1



    

    

    







    