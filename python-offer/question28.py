#对称的二叉树

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

def symmetric_tree(tree_root1,tree_root2):
    if tree_root1 is None and tree_root2 is None:
        return True
    if tree_root1 is None or tree_root2 is None:
        return False
    if tree_root1._item != tree_root2._item:
        return False
    return symmetric_tree(tree_root1._left,tree_root2._right) and symmetric_tree(tree_root1._right,tree_root2._left)


if __name__ == "__main__":
    node11 = TreeNode(8)
    node12 = TreeNode(6)
    node13 = TreeNode(6)
    node14 = TreeNode(5)
    node15 = TreeNode(7)
    node16 = TreeNode(7)
    node17 = TreeNode(5)
    node21 = TreeNode(8)
    node22 = TreeNode(6)
    node23 = TreeNode(9)
    node24 = TreeNode(5)
    node25 = TreeNode(7)
    node26 = TreeNode(7)
    node27 = TreeNode(5)
    node31 = TreeNode(7)
    node32 = TreeNode(7)
    node33 = TreeNode(7)
    node34 = TreeNode(7)
    node35 = TreeNode(7)
    node36 = TreeNode(7)
    node11._left = node12
    node11._right = node13
    node12._left = node14
    node12._right = node15
    node13._left = node16
    node13._right = node17
    node21._left = node22
    node21._right = node23
    node22._left = node24
    node22._right = node25
    node23._left = node26
    node23._right = node27
    node31._left = node32
    node31._right = node33
    node32._left = node34
    node32_right = node35
    node33._left = node36
    tree1 = Tree()
    tree1._root = node11
    tree2 = Tree()
    tree2._root = node21
    tree3 = Tree()
    tree3._root = node31
    print(tree1.bfs())
    print(tree2.bfs())
    print(tree3.bfs())
    print(symmetric_tree(node11,node11))
    print(symmetric_tree(node21,node21))
    print(symmetric_tree(node31,node31))
  
