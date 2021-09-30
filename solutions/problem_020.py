'''
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{} ->".format(node.val)
            node = node.next
        string += "None]"
        return string


def get_nodes(values):
    next_node = None
    for value in values[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node


def get_list(head):
    node = head
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next
    return nodes


def get_intersection_node(list_a, list_b):

    def get_list_length(linked_list):
        length = 0
        node = linked_list
        while node:
            length += 1
            node = node.next

        return length

    len_a, len_b = get_list_length(list_a), get_list_length(list_b)
    min_len = min(len_a, len_b)

    for _ in range(len_a - min_len):
        list_a = list_a.next
    for _ in range(len_b - min_len):
        list_b = list_b.next

    node_a = list_a
    node_b = list_b
    for _ in range(min_len):
        if node_a.val == node_b.val:
            return node_a
        node_a = node_a.next
        node_b = node_b.next

    return None


assert not get_intersection_node(
    get_nodes([]), get_nodes([]))
assert get_intersection_node(
    get_nodes([0, 3, 7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
assert get_intersection_node(
    get_nodes([7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
'''


class Node:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def printLinkedList(node):
	while node:
		print(node.val,'->' ,end='')
		node=node.next
	print()

def findIntersectNodeWithSet(node1,node2):
	mset=set()
	node=node1
	while node:
		mset.add(node)
		node=node.next

	node=node2
	while node and node not in mset:
		node=node.next

	if node in mset:
		return node

	return None

def countNode(root):	
	node=root
	count=0
	while node:
		count+=1
		node=node.next


	print(count)
	return count

def findIntersectNode(node1,node2):
	n1=countNode(node1)
	n2=countNode(node2)
	longnode,shortnode,difcount = (node1,node2,n1-n2) if n1>n2 else (node2,node1,n2-n1)

	count=0
	while count<difcount and longnode:
		count+=1
		longnode=longnode.next

	while longnode:
		if longnode.val==shortnode.val:
			return longnode
		longnode=longnode.next
		shortnode=shortnode.next

	return None

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
node8=Node(8,Node(10))
node7=Node(7,node8)
node1=Node(1,node8)
node3=Node(3,node7)
node99=Node(99,node1)


printLinkedList(findIntersectNode(node3,node99))
