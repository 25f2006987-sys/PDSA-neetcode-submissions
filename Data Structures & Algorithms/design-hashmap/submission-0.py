class MyHashMap:

    def __init__(self):
        self.hashmap=[]
        

    def put(self, key: int, value: int) -> None:
        for k in self.hashmap:
            if k[0]==key:
                k[1]=value
                return
        self.hashmap.append([key,value])
            
        

    def get(self, key: int) -> int:
        for k in self.hashmap:
            if k[0]==key:
                return k[1]
                
        return -1
        
        

    def remove(self, key: int) -> None:
        for k in self.hashmap:
            if k[0]==key:
                self.hashmap.remove(k)
                
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)