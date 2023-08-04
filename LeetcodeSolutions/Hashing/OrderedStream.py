class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        #Defines an empty list of lists sized n and a pointer at index 0
        self.stream = [None] * n
        self.ptr = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        #simply insert to the lsit
        idKey -= 1
        self.stream[idKey] = value
        #check to see if the pointer is less than the key, if so return an empty list
        if self.ptr < idKey:
            return []
        #if not, return a slice from the id to the point where it's not none
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[idKey:self.ptr]
        
obj = OrderedStream(5)
print(obj.insert(3, "ccccc"))
print(obj.insert(1, "aaaaa"))
print(obj.insert(2, "bbbbb"))
print(obj.insert(5, "eeeee"))
print(obj.insert(4, "ddddd"))