'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

def count_unival_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_unival_trees(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_unival_trees(root.left)
    
    child_counts = count_unival_trees(root.left) + count_unival_trees(root.right)
    current_node_count = 0
    if root.data == root.left.data and root.data == root.left.data:
        current_node_count = 1

    return current_node_count + child_counts


node_a = Node('0')
node_b = Node('1')
node_c = Node('0')
node_d = Node('1')
node_e = Node('0')
node_f = Node('1')
node_g = Node('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

assert count_unival_trees(None) == 0
assert count_unival_trees(node_a) == 5
assert count_unival_trees(node_c) == 4
assert count_unival_trees(node_g) == 1
assert count_unival_trees(node_d) == 3
'''

#https://crazycoderzz.wordpress.com/count-the-number-of-unival-subtrees-in-a-binary-tree/
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def countUnivalSubtree(node):
    _,count=__countUnivalSubtree(node)
    return count

def __countUnivalSubtree(node):
    if not node:
        return (True,0)
    
    leftcheck,leftcount=__countUnivalSubtree(node.left)
    rightcheck,rightcount=__countUnivalSubtree(node.right)

    if not leftcheck or not rightcheck:
        return (False,leftcount+rightcount)
    
    if node.left and node.left.val!=node.val:
        return (False,leftcount+rightcount)

    if node.right and node.right.val!=node.val:
        return (False,leftcount+rightcount)

    return (True,leftcount+rightcount+1)

node = Node(0,
        Node(1),
        Node(0,
            Node(1,
                Node(1),
                Node(1)
            ),
            Node(0)
        )
    )
assert countUnivalSubtree(node)==5

node = Node(0,
        Node(1),
        Node(0,
            Node(0,
                Node(1),
                Node(1)
            ),
            Node(0)
        )
    )
assert countUnivalSubtree(node)==4

node = Node(0,
        Node(1),
        Node(0,
            Node(0,
                Node(1),
                Node(1)
            ),
            Node(0,
                Node(1),
                Node(1)
            )
        )
    )
assert countUnivalSubtree(node)==5

node = Node(0,
        Node(1),
        Node(0,
            Node(1,
                Node(1),
                Node(1)
            ),
            Node(1,
                Node(1),
                Node(1)
            )
        )
    )
assert countUnivalSubtree(node)==7
