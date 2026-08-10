class MyHashSet:

    def __init__(self):
        # Number of buckets in the hash table
        self.size = 100000
        # Create an empty list for every bucket.
        # Each bucket stores keys that have the same hash index.
        self.buckets=[[] for i in range(self.size)]
    def hash_val(self,key):
     # Convert the key into a valid bucket index.
        return key%self.size  

    def add(self, key: int) -> None:
    # Find the bucket where this key should be stored.
        index=self.hash_val(key)
    # Add the key only if it is not already in the bucket.
        # This prevents duplicate values in the set.
        if key not in self.buckets[index]:
            self.buckets[index].append(key)


    def remove(self, key: int) -> None:
        index=self.hash_val(key)
    #if index is not empty check for the valid key.
        if  self.buckets[index]!=None:
# We use a while loop to check the entire bucket.
# If duplicate keys exist, remove all matching occurrences.
# This ensures that the key is completely removed from the HashSet.
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