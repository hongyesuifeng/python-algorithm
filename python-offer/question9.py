class stack():
    def __init__(self):
        self._item = []
   
    def push(self,item):
        self._item.append(item)

    def pop(self):
        return self._item.pop()

    def is_empty(self):
        return len(self._item) == 0
    
    def print_all(self):
        print(self._item)

class Queue():
    def __init__(self):
        self._stack1 = stack()
        self._stack2 = stack()
   
    def enqueue(self,item):
        self._stack1.push(item)

    def dequeue(self):
        if not self._stack2.is_empty():
            return self._stack2.pop()
        else:
            while not self._stack1.is_empty():
                self._stack2.push(self._stack1.pop())
            if not self._stack2.is_empty():
                return self._stack2.pop()
            else:
                return None

    def print_two_stack(self):
        print("this is first stack:")
        self._stack1.print_all()
        print("this is second stack:")
        self._stack2.print_all()

if __name__ == "__main__":
    queue = Queue()
    queue.print_two_stack()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.print_two_stack()
    queue.dequeue()
    queue.print_two_stack()
    queue.dequeue()
    queue.print_two_stack()
    queue.dequeue()
    queue.print_two_stack()
