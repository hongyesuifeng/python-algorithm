#反转链表

class Node():
    def __init__(self,item,next_node=None):
        self._item = item
        self._next = next_node
   
    def __repr__(self):
        return str(self._item)


class LinkList():
    def __init__(self):
        self._head = None
        self.length = 0
    
    def append(self,item):
        if isinstance(item,Node):
            node = item
        else:
            node = Node(item)
        if self._head == None:
            self._head = node
        else:
            insert_node = self._head
            while insert_node._next:
                insert_node = insert_node._next
            insert_node._next = node
        self.length += 1

    def print(self):
        if self._head == None:
            print("Is empty")
        elif self._head._next == None:
            print(self._head._item)
        else:
            print_node = self._head
            while print_node._next:
                print(print_node._item, end="->")
                print_node = print_node._next
            print(print_node._item)

    def reverse_link_list(self):
        pre_node = None
        node = self._head
        while node is not None: 
            print(node)
            next_node = node._next
            node._next = pre_node
            pre_node = node
            node = next_node
        self._head = pre_node

if __name__ == "__main__":
    Nodea = Node('a')
    Nodef = Node('f')
    link_list = LinkList()
    link_list.append(Nodea)
    link_list.append('b')
    link_list.append('c')
    link_list.append('d')
    link_list.append('e')
    link_list.append(Nodef)
    link_list.print()
    link_list.reverse_link_list()
    link_list.print()
