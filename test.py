#implement a LRU cache

#support function of accessing a key-value
#getting/value

#stack 
#LRU pull from the middle 

# 
# 2 : orange    [0] 
# 1 : apple     [1]
# 3 : grape     [2]
# defaultdict

#linked list with dictionary
#explain why this data structure would work
#clarify why im using the data structure


from typing import OrderedDict

#popitem pops off the right side (end)
#move_to_end which moves the element to the end or the beginning

#explain before i type
#having a visual much better
#ask if i can turn on screen share for a drawing application

#before i code

class LRU:
    def __init__(self,n):
        self.max = n
        self.dict = OrderedDict()
        
    def set(self, k, v):
        if k in self.dict:
            self.dict.move_to_end(k, last = False)
        else:
            self.dict[k] = v
            self.dict.move_to_end(k, last = False)
            
        #maintain the size of the cache
        if len(self.stack) > self.max:
            self.dict.popitem()
            
    def get(self, k): #this is bad time complex
        if k in self.dict:
            return self.dict[k]
        
        assert("Not in dictionary")