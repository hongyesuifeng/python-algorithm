#从尾到头打印链表

class Node():
    def __init__(self,item,next_node=None):
        self._item = item
        self._next = next_node
   
    def __repr__(self):
        return str(self._item)


class Stack():
    def __init__(self):
        self._item = []
    def is_empty(self):
        return len(self._item) == 0
    def push(self,item):
        self._item.append(item)
    def pop(self):
        return self._item.pop()


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
            
    def reversal_print(self):
        if self._head == None:
            print("Is empty")
        elif self._head._next == None:
            print(self._head._item)
        else:
            reversal_stack = Stack()
            print_node = self._head
            while print_node._next:
                reversal_stack.push(print_node._item)
                print_node = print_node._next
            reversal_stack.push(print_node._item)
        while(not reversal_stack.is_empty()):
           print(reversal_stack.pop(), end=" ")
        print("")      

if __name__ == "__main__":
    link_list = LinkList()
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.print()
    link_list.reversal_print() 
