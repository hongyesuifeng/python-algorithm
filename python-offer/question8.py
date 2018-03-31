#二叉树的下一个节点
from collections import deque 

class TreeNode():
    def __init__(self,item):
        self._item = item
        self._left = None
        self._right = None
        self._father = None
    def __repr__(self):
        return self._item


class Tree():
    def __init__(self):
        self._root = None

    def bfs(self):
        ret = []
        queue = deque([self._root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node._item)
                queue.append(node._left)
                queue.append(node._right)
        return ret


def binary_tree_next_node(tree,Node):
    if not tree:
        return None
    Node = Node
    if Node._right:
        Node_right = Node._right
        while(Node_right._left):
            Node_right = Node_right._left
        return Node_right
    elif Node == Node._father._left:
        return Node._father
    else:
        Node_father = Node._father
        while(Node_father._father):
            if Node_father == Node_father._father._left:
                return Node_father._father
            Node_father = Node_father._father
    return None

if __name__ == "__main__":
    t = Tree()
    Nodea = TreeNode('a')
    Nodeb = TreeNode('b')
    Nodec = TreeNode('c')
    Noded = TreeNode('d')
    Nodee = TreeNode('e')
    Nodef = TreeNode('f')
    Nodeg = TreeNode('g')
    Nodeh = TreeNode('h')
    Nodei = TreeNode('i')
    Nodea._left = Nodeb
    Nodea._right = Nodec
    Nodeb._left = Noded
    Nodeb._right = Nodee
    Nodeb_father = Nodea
    Nodec._left = Nodef
    Nodec._right = Nodeg
    Nodec._father = Nodea
    Noded._father = Nodeb
    Nodee._left = Nodeh
    Nodee._right = Nodei
    Nodee._father = Nodeb
    Nodef._father = Nodec
    Nodeg._father = Nodec
    Nodeh._father = Nodee
    Nodei._father = Nodee
    t = Tree()
    t._root = Nodea
    print(t.bfs())
    print(binary_tree_next_node(t,Noded)) 
    print(binary_tree_next_node(t,Nodeb)) 
    print(binary_tree_next_node(t,Nodeh)) 
    print(binary_tree_next_node(t,Nodee)) 
    print(binary_tree_next_node(t,Nodei)) 
    print(binary_tree_next_node(t,Nodea)) 
    print(binary_tree_next_node(t,Nodef)) 
    print(binary_tree_next_node(t,Nodec)) 
    print(binary_tree_next_node(t,Nodeg)) 
