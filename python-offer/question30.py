#包含min函数的栈

class stack():
    def __init__(self):
        self._item = []
        self._min = []

    def pop(self):
        if self._item:
            self._min.pop()
            return self._item.pop()
        else:
            print("stack is empty!")

    def push(self,item):
        self._item.append(item)
        self._min.append(min(self._item))
    
    def min(self):
        if self._min:
            return self._min[-1]
        else:
            print("min stack is empty!")

    def print_all(self):
        print("this is stack: ", self._item)
        print("this is min_stack: ", self._min)


if __name__ == "__main__":
    stack = stack()
    stack.min()
    stack.print_all()
    stack.push(3)
    stack.min()
    stack.print_all()
    stack.push(4)
    stack.min()
    stack.print_all()
    stack.push(2)
    stack.min()
    stack.print_all()
    stack.push(1)
    stack.min()
    stack.print_all()
    stack.pop()
    stack.min()
    stack.print_all()
    stack.pop()
    stack.min()
    stack.print_all()
    stack.push(0)
    stack.min()
    stack.print_all()
