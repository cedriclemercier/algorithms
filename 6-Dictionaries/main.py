keys = [12,14,3,6,9,2,11,10,4]


m = 11
hashtable = {}
for i in range(m):
    hashtable[i] = ""


def insert(hashtable, keys):
    for key, value in hashtable.items():
        


for key, value in hashtable.items():
    print(f"'{key}':{value}")


def delete(hashtable, key):
    mod = key % m
    for i in range(m):
        print(hashtable[mod+i])
        if hashtable[mod+i][0] == key:
            hashtable[mod+i][0] = 'delete'


#delete(hashtable, 4)


for key, value in hashtable.items():
    print(f"'{key}': {value}")
