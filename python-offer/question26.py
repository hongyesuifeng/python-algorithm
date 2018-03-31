#树的子结构


from collections import deque
from anytree import Node, RenderTree

class TreeNode():
    def __init__(self,item):
        self._item = item 
        self._left = None
        self._right = None


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

def has_subtree(tree1_root,tree2_root):
    result = False
    if tree1_root._item == tree2_root._item:
        result = has_subtree_core(tree1_root,tree2_root)
    if not result:
        result = has_subtree(tree1_root._left,tree2_root) or has_subtree(tree1_root._right,tree2_root)
    return result

def has_subtree_core(tree1_root,tree2_root):
    if tree2_root is None:
        return True
    if tree1_root is None:
        return False
    if tree1_root._item != tree2_root._item:
        return False
    return has_subtree_core(tree1_root._left,tree2_root._left) and has_subtree_core(tree1_root._right,tree2_root._right)

if __name__ == "__main__":
    tree11 = TreeNode('8')
    tree12 = TreeNode('8')
    tree13 = TreeNode('7')
    tree14 = TreeNode('9')
    tree15 = TreeNode('2')
    tree16 = TreeNode('4')
    tree17 = TreeNode('7')
    tree21 = TreeNode('8')
    tree22 = TreeNode('9')
    tree23 = TreeNode('2')
    tree11._left = tree12
    tree11._right = tree13
    tree12._left = tree14
    tree12._right = tree15
    tree15._left = tree16
    tree15._right = tree17
    tree21._left = tree22
    tree21._right = tree23
    tree1 = Tree()
    tree1._root = tree11
    tree2 = Tree()
    tree2._root = tree21   
    print(tree1.bfs())
    print(tree2.bfs())
    print(has_subtree(tree11,tree21)) 
