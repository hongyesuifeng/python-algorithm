#二叉树的镜像 

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

def mirror_tree(tree_root):
    if tree_root._left is None and tree_root._right is None:
        return
    temp = tree_root._left
    tree_root._left = tree_root._right
    tree_root._right = temp
    if tree_root._left:
        mirror_tree(tree_root._left)
    if tree_root._right:
        mirror_tree(tree_root._right)

if __name__ == "__main__":
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)
    node1._left = node2
    node1._right = node3
    node2._left = node4
    node2._right = node5
    node3._left = node6
    node3._right = node7
    tree = Tree()
    tree._root = node1
    print(tree.bfs())
    mirror_tree(node1)
    print(tree.bfs())
