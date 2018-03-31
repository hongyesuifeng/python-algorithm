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
                print(print_node._item, end=" ")
                print_node = print_node._next
            print(print_node._item)

def find_kth_to_tail(head_node,k):
    node = head_node
    length = 1
    while node._next is not None:
        node = node._next
        length += 1
    if k > length:
        return False
    for i in range(length-k):
        head_node = head_node._next
    return head_node._item

if __name__ == "__main__":
    Link_list = LinkList()
    Nodea = Node('a')
    Link_list.append(Nodea)
    Link_list.append('b')
    Link_list.append('c')
    Link_list.append('d')
    Link_list.append('e')
    Link_list.append('f')
    Link_list.print()
    print(find_kth_to_tail(Nodea,1))
    print(find_kth_to_tail(Nodea,3))
    print(find_kth_to_tail(Nodea,5))
    print(find_kth_to_tail(Nodea,6))
    print(find_kth_to_tail(Nodea,7))
