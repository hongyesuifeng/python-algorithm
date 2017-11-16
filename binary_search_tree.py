class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, new_val):
        return self.insert_help(self.root, new_val)

    def insert_help(self, start, new_val):
        if start:
            if start.value > new_val:
                self.insert_help(start.left, new_val)
            elif self.root.value < new_val:
                self.insert_help(start.right, new_val)
        else:
            start = Node(new_val)
            
    def search(self, find_val):
        return self.search_help(self.root, find_val)

    def search_help(self, start, find_val):
        if start:
            if self.root.value == find_val:
                return True
            elif self.root.value > find_val:
                return self.search_help(start.left, find_val)
            else:
                return self.search_help(start.right, find_val)
        else:
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
print(tree.search(4))
# Should be False
print(tree.search(6))
