#栈的压入、弹出序列


class stack():
    def __init__(self):
        self._item = []

    def pop(self):
        if self._item:
            return self._item.pop()
        else:
            print("stack is empty!")

    def push(self,item):
        self._item.append(item)

    def top(self):
        if self._item:
            return self._item[-1]
        else:
            return None
    
    def print_all(self):
        print("this is stack: ", self._item)

def is_order(push_order,pop_order):
    tmp_stack = stack()
    while pop_order:
        if pop_order[0] == tmp_stack.top():
            pop_order.pop(0)
            tmp_stack.pop()
        else:
            tmp_stack.push(push_order.pop(0))
        if not push_order and pop_order and tmp_stack and pop_order[0] != tmp_stack.top():
            return False
        print("this is push_order: ", push_order)
        tmp_stack.print_all()
        print("this is pop_order: ", pop_order)
    
    if not pop_order:
        return True
          

if __name__ == "__main__":
    print(is_order([1,2,3,4,5],[4,5,3,2,1]))
    print(is_order([1,2,3,4,5],[4,3,5,1,2])) 
