import json

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

def serialize(root):
    if not root:
        return None

    serialized_tree_map = dict()
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    serialized_tree_map['data'] = root.data
    if serialized_left:
        serialized_tree_map['left'] = serialized_left
    if serialized_right:
        serialized_tree_map['right'] = serialized_right

    return json.dumps(serialized_tree_map)


def deserialize(s):
    serialized_tree_map = json.loads(s)

    node = Node(serialized_tree_map['data'])
    if 'left' in serialized_tree_map:
        node.left = deserialize(serialized_tree_map['left'])
    if 'right' in serialized_tree_map:
        node.right = deserialize(serialized_tree_map['right'])

    return node


node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

serialized_a = serialize(node_a)
print(serialized_a)

deserialized_a = deserialize(serialized_a)
assert str(deserialized_a) == "a"



'''
# do not use dictionary , only serialize and deserialize in the order
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def serialize(node):
		if not node:
			return ''
		return f'{node.val},{Node.serialize(node.left)},{Node.serialize(node.right)}'

	def __repr__(self):
		return Node.serialize(self)

	def deserialize(s):
		if not s:
			return
		return Node.deserialize_list(s.split(','))

	def deserialize_list(s):
		val=s.pop(0)
		if not val:
			return
			
		node=Node(val)
		node.left = Node.deserialize_list(s)
		node.right= Node.deserialize_list(s)
		return node		

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')

node_a.left = node_b
node_a.right = node_c

node_b.left = node_d
node_b.right = node_e

node_c.left = node_f
node_c.right = node_g

print(node_a)
print(Node.deserialize(str(node_a)))
assert Node.deserialize(str(node_a)).val == "a"
'''
