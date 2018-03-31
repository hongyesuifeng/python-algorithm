#重建二叉树
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

   
def re_construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    inorder_left = inorder[:index]
    inorder_right = inorder[index+1:]
    root = TreeNode(preorder[0])
    root._left = re_construct_tree(preorder[1:1+len(inorder_left)], inorder_left)
    root._right = re_construct_tree(preorder[1+len(inorder_left):], inorder_right)
    return root

if __name__ == "__main__":
    t = Tree()
    root = re_construct_tree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    t._root = root
    print(t.bfs())
