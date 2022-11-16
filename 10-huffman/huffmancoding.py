from collections import Counter

#every node object will have two children, otherwise is a leave
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def getChild(self):
        return self.left, self.right

def get_code(node, code = ''):
    
    if type(node) is str:
        #stop!!!
        return {node : code}
    
    #get the children
    left, right = node.getChild()
    
    #recursive function
    huffman_code = dict()
    huffman_code.update(get_code(left, code+'0'))
    huffman_code.update(get_code(right, code+'1'))
    
    return huffman_code

def decode(encoded_message, root_tree):
    original_root = root_tree
    decoded_message = []
    for e in encoded_message:
        
        if e == '0':
            root_tree = root_tree.left
        elif e =='1':
            root_tree = root_tree.right
        
        if type(root_tree) is str:
            decoded_message.append(root_tree)
            root_tree = original_root
            continue
            
    return decoded_message
            

def calculateTotalCost(message, code=None):
    if code is None:
        return len(message) * 8

    return len(message)
    
    
    

def encode(message, h):
    encoded_message = ''
    for m in message:
        encoded_message += h[m]
    return encoded_message

def make_the_tree(freqs_sorted):
    
    #as long as freqs_sorted.length > 1
    while len(freqs_sorted) > 1:
        
        #combine the two smallest one
        key1, value1 =  freqs_sorted[0]
        key2, value2 =  freqs_sorted[1]
        
        #delete them
        freqs_sorted = freqs_sorted[2:]
        
        #add the new combination to freqs_sorted
        new_value = value1 + value2
        new_node  = Node(key1, key2)
        
        #add to freqs_sorted
        freqs_sorted.append((new_node, new_value))
                
        #sort again!!
        freqs_sorted = sorted(freqs_sorted, key=lambda item: item[1])
        
    return freqs_sorted[0][0]
    #return root node (so we can use this generating coding....)

#input
message = 'AAABBBBBBEEEDABEEDCC'

#count the letters
#use Counter, then convert to dictionary
freqs = dict(Counter(message)) #{'A': 4, 'B': 7, 'E': 5, 'D': 2, 'C': 2}
# print(freqs['A'])  #4

#sort them from smallest to biggest
#{'C': 2, 'D': 2, 'A': 4, 'E': 5, 'A': 7}
freqs_sorted = sorted(freqs.items(), key=lambda item: item[1])

#make the tree by combining the smallest one, and delete those guys
root = make_the_tree(freqs_sorted)
# print(root.getChild()[0].getChild()[1].getChild())
# print(root.left.left)

#get the code
huffman_code = get_code(root)

#print the code
print(huffman_code)
#{'A': '01'; 'B': '11'; 'C': '000'; 'D': '001'; 'E': '10'}
encoded_message = encode(message, huffman_code)
print(encoded_message)

#task1: decode the encoded message to the original message
original_message = decode(encoded_message, root)
print('Original Message Decoded:', ''.join(original_message))

#task2: calculate the total cost --> message + table
print('Total cost original message', calculateTotalCost(message))
print('Total cost encoded message', calculateTotalCost(encoded_message, huffman_code))