class MyHashSet:

    def __init__(self):
        self.size=10000
        self.buckets=[[] for i in range(self.size)]
    def hash_val(self,key):
        return key%self.size  

    def add(self, key: int) -> None:
        index=self.hash_val(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)


    def remove(self, key: int) -> None:
        index=self.hash_val(key)
        if  self.buckets[index]!=None:
            while key in self.buckets[index]:
                self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index=self.hash_val(key)
        return key in self.buckets[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)