#删除链表的节点
class Node():
    def __init__(self, item):
        self._item = item
        self._next = None
    
    def __repr__(self):
        return str(self._item)

class LinkList():
    def __init__(self):
        self._head = None
        self._length = 0
    
    def is_empty(self):
        return self._length == 0
    
    def append(self, item):
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
        self._length += 1

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

    def pop_head_item(self):
        if self._head == None:
            return None
        else:
            number = self._head._item
            self._head = self._head._next
            return number


def delete_node(head_node, delete_node):
    if head_node is None or delete_node is None:
        return None
    if delete_node._next is not None:
        next_node = delete_node._next
        delete_node._item = next_node._item
        delete_node._next = next_node._next
        next_node._next = None
    elif head_node == delete_node:
        head_node._item = None
    else:
        find_node = head_node
        while find_node._next != delete_node:
            find_node = find_node._next
        find_node._next = None

if __name__ == "__main__":
    link_list = LinkList()
    Nodea = Node('a')
    Nodeb = Node('b')
    Nodec = Node('c')
    Noded = Node('d')
    Nodee = Node('e')
    Nodef = Node('f')
    Nodeg = Node('g')
    link_list.append(Nodea)
    link_list.append(Nodeb)
    link_list.append(Nodec)
    link_list.append(Noded)
    link_list.append(Nodee)
    link_list.append(Nodef)
    link_list.append(Nodeg)
    link_list.print()
    delete_node(Nodea,Nodeb)
    link_list.print()
    delete_node(Nodea,Nodeg) 
    link_list.print()
    delete_node(Nodea,Nodea)
    link_list.print()
