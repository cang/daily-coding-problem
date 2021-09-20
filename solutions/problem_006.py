class Node:
    def __init__(self, data):
        self.data = data
        self.both = id(data)

    def __repr__(self):
        return str(self.data)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

# id_map simulates object pointer values
id_map = dict()
id_map[id("a")] = a
id_map[id("b")] = b
id_map[id("c")] = c
id_map[id("d")] = d
id_map[id("e")] = e


class LinkedList:

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.data)
            result_node = id_map[next_node_address]
        return result_node.data


llist = LinkedList(c)
llist.add(d)
llist.add(e)
llist.add(a)

assert llist.get(0) == "c"
assert llist.get(1) == "d"
assert llist.get(2) == "e"
assert llist.get(3) == "a"




'''
Node A: npx(A)= 0 XOR add(B)
Node B: npx(B)= add(A) XOR add(C)
Node C: npx(C)= add(B) XOR add(D)
Node D: npx(D)= add(C) XOR 0

npx(C) XOR add(B)
<=> ( add(B) XOR add(D) ) XOR add(B) // npx(C) = add(B) XOR add(D)
<=> add(B) XOR add(D) XOR add(B) // (a^b)^c = a^b^c
<=> add(D) XOR add(B) XOR add(B) // a^b = b^a
<=> add(D) XOR 0 //a^a = 0
<=> add(D) // a^0 = a


'''

import ctypes

def addressOf(obj):
    if obj:
        return id(obj)
    return 0
def getObject(obj_id):
    if obj_id:
        return ctypes.cast(obj_id, ctypes.py_object).value
    return None

class XORNode:
    def __init__(self,val):
        self.val=val
        self.npx=0
    def __repr__(self):
        return f"val={self.val},npx={self.npx}"

class XORLinkedList:
    def __init__(self):
        self.__nodes = [] # this array keep nodes has not been release
        self.head=self.tail=None

    def add(self,val):
        node = XORNode(val)
        node.npx=addressOf(self.tail) ^ addressOf(None)

        if self.tail:
            #self.tail.npx=self.tail.npx^addressOf(node)
            previd = self.tail.npx^addressOf(None)
            nextid = addressOf(node)
            self.tail.npx=previd^nextid

        self.__nodes.append(node)
        self.tail = node
        
        if not self.head:
            self.head=node

    def get(self,i):
        #return self.__nodes[i]
        if not self.head:
            return None

        cur = self.head
        previd=addressOf(None)

        count=0

        while cur:
            if count==i:
                return cur

            nextid = previd^cur.npx
            previd = addressOf(cur)
            cur=getObject(nextid)
            count+=1
        
        return None
    
xorlink = XORLinkedList()
xorlink.add(100)
xorlink.add(200)
xorlink.add(300)

assert xorlink.get(1).val==200

