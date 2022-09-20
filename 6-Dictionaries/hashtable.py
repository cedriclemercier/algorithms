'''

Assignment: Linear probing

'''


class Hashtable:

    def __init__(self, m):
        self.m = m
        self.hashtable = self.create_hash_table()


    def create_hash_table(self):
        return [[] for _ in range(self.m)]
    
    
    def _hash(self, key):
        # get the position using division method
        index = key % self.m
        bucket = self.hashtable[index]
        
        return bucket
    
    
    def _prehash(self, key):
        if (type(key) == str):
            key = hash(key) # return a number

        # challenge: handle negative keys and string
        if ((type(key) == int) or (type(key) == float)):
            if key < 0:
                key = hash(float(key)) * -1 #first convert to float, then hash it

        
        print("After prehash:", key)
        assert (key > 0) & (type(key) == int)
        return key

    def insert(self, key, value):

        key = self._prehash(key)
        bucket = self._hash(key)

        #CEHCK WHETER THE KEY DUPLICATES
        found, position_duplicate, _ = self.search(key)
        
        # if they key duplicates only update the value
        if (found):
            bucket[position_duplicate] = (key, value)
        else:
            bucket.append((key, value))

        print(self.hashtable)



    def search(self, key):
        
        key = self._prehash(key)
        
        bucket = self._hash(key)
        
        found=False
        answer = -999
        pos_dup = None

        for i, (bkey, bval) in enumerate(bucket):
            if bkey==key:
                found = True
                answer = bval
                pos_dup = i
        
        return found, pos_dup, answer 


    def delete(self, key):
        pass

    
    def print(self):
        print(self.hashtable)



ht = Hashtable(3)
print(ht.hashtable)
ht.insert(1, 'Chaky')
ht.insert(2, 'peter')
ht.insert(2, 'petterssss')
ht.insert(3, 'john')
ht.insert(12, 'matt')

print(ht.search(12))




# assignment linear probing
# add delete
# fix search? delete flag
# make sure m >>>>>>> than param number
