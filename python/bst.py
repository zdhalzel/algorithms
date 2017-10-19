'''Inspired by Udacity Technical Interview course'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_insert(self, start, val):
        if val < start.value:
            if start.left is None:
                start.left = Node(val)
            else:
                self.bst_insert(start.left, val)
        if val > start.value:
            if start.right is None:
                start.right = Node(val)
            else:
                self.bst_insert(start.right, val)

    def bst_search(self, start, val):
        if start:
            if start.value is val: return True
            if val < start.value:
                return self.bst_search(start.left, val)
            if val > start.value:
                return self.bst_search(start.right, val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print
tree.search(4)
# Should be False
print
tree.search(6)