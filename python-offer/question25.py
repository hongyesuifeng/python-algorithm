#合并两个排序的链表
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

    def pop_head_item(self):
        if self._head == None:
            return None
        else:
            number = self._head._item
            self._head = self._head._next
            return number
  
def merge_two_link_list(link_list1,link_list2):
    last_list = []
    while link_list1._head is not None:
        last_list.append(link_list1.pop_head_item())
    while link_list2._head is not None:
        last_list.append(link_list2.pop_head_item())
    last_list.sort()
    link_list = LinkList()
    for each in last_list:
        link_list.append(each)
    return link_list

if __name__ == "__main__":
    link_list1 = LinkList()
    link_list2 = LinkList()
    link_list1.append(1)
    link_list1.append(3)
    link_list1.append(5)
    link_list1.append(7)
    link_list2.append(2)
    link_list2.append(4)
    link_list2.append(6)
    link_list2.append(8)
    link_list1.print()
    link_list2.print()
    link_list = merge_two_link_list(link_list1,link_list2)
    link_list.print()
