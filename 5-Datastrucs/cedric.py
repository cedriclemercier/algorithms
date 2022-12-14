

class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        # if we have a root node
        if (self.key):
            # then check left and right
            
            # condition 1: if less than: go left
            if (key < self.key):
                #cond1.1: if the left is NIL, fill it\
                if (self.left == None):
                    self.left = Node(key)
                #cond1.2: if left is not nill, oh no
                else:
                    self.left.insert(key)
            # condition 2: if greater than: go right
            
            elif(key >= self.key):
                #cond1.2: if the right is nill fill it
                if (self.right == None):
                    self.right = Node(key)
                #cond2.2: if the right is not nill, consider right as parent
                else:
                    self.right.insert(key)


        # if we dont ahve a root node
        else:
            # set root node
            self.key = key




    def printT(self):
        #print left
        if (self.left):
            self.left.printT()
        print(self.key)
        #print middle

        #print right
        if (self.right):
            self.right.printT()


        #hint:use recursion

    def delete(self,key):
        # if this is the key we look for:
        if self.key == key:
            # if there are left and right nodes
            if self.right and self.left: 
                # pass the parent and recursively find the leftmost minimum array in right
                [psucc, succ] = self.right.find_min(self)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                succ.left = self.left
                succ.right = self.right

                return succ                

            else:
                if self.left:
                    return self.left    
                else:
                    return self.right   
        
        # if the key is smaller go to the left
        else:
            if self.key > key:          
                if self.left:
                    self.left = self.left.delete(key)
            #otherwise go the right
            else:                      
                if self.right:
                    self.right = self.right.delete(key)

        return self
                

    def successor(self):
        pass


def find_min(self, parent):
    if self.left:
        return self.left.find_min(self)
    else:
        return [parent, self]

# -1
# 1
# 2
# 4
# 5
# 6
# 10

#try our class
root = Node(1)
list = [4,10,-1,5,6,2]
print("Inserting list", str(list))
for i in list:
    root.insert(i)
print("Tree is: \n")
root.printT()
print("Removing 2")
root.delete(2)
root.printT()
