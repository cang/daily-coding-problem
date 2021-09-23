'''
def add_to_trie(s, trie):
    if not s:
        return trie

    character = s[0]
    if character not in trie:
        trie[character] = dict()
    
    trie[character] = add_to_trie(s[1:], trie[character])

    return trie

def get_dictionary_trie(dictionary):
    trie = dict()
    for word in dictionary:
        trie = add_to_trie(word, trie)

    return trie

def get_possible_completions(trie):
    possible_completions = list()
    for character in trie:
        if trie[character]:
            child_completions = get_possible_completions(trie[character])
            for child_completion in child_completions:
                possible_completions.append(character + child_completion)
        else:
            possible_completions.append(character)
        
    return possible_completions

def get_autocomplete_suggestions(s, dictionary):
    trie = get_dictionary_trie(dictionary)

    current_trie = trie
    for character in s:
        if character not in current_trie:
            return []
        current_trie = current_trie[character]

    completions = get_possible_completions(current_trie)
    completions = [s + x for x in completions]

    return completions 

assert get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
assert get_autocomplete_suggestions("ae", []) == []
'''



'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''
#from typing import Callable, Iterator, Union, Optional, List, Any
from typing import Optional, List, Any

class Node:
    def __init__(self) -> None:
        self.children: Dict[str, Node] = {}
        self.value: Optional[Any] = None

def insert(node: Node, key: str, value: Any) -> None:
	for ch in key:
		if ch not in node.children:
			node.children[ch]=Node()
		node = node.children[ch]
	node.value=value

def get_node(node: Node, key: str) -> Optional[Node]:
    """
    Find node by key. This is the same as the `find` function defined above,
    but returning the found node itself rather than the found node's value.
    """
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node    

def keys_with_prefix(root: Node, prefix: str) -> List[str]:
    results: List[str] = []
    x = get_node(root, prefix)
    _collect(x, list(prefix), results)
    return results

def _collect(x: Optional[Node], prefix: List[str], results: List[str]) -> None:
    """
    Append keys under node `x` matching the given prefix to `results`.
    prefix: list of characters
    """
    print(prefix)

    if x is None:
        return
    if x.value is not None:
        prefix_str = ''.join(prefix)
        results.append(prefix_str)
        print(prefix_str)

    for c in x.children:
        prefix.append(c)
        _collect(x.children[c], prefix, results)
        del prefix[-1]  # delete last character

def printnode(node: Node,tb: str):
    if not node: return
    if node.value:
        print(tb,node.value)
    for k,v in node.children.items():
        print(tb,k,'->')
        printnode(v,tb+'\t')

node = Node()
insert(node,'dog','dog')
insert(node,'deer','deer')
insert(node,'deal','deal')
printnode(node,'')


print(keys_with_prefix(node,'de'))

