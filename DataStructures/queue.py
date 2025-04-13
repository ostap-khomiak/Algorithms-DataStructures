class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Queue - FIFO
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # deque
    def get(self):  
        h = self.head
        self.head = h.next
        h.next = None
        self.length -= 1
        return h.data
    
    # enqueue
    def add(self, data): 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def __str__(self):
        node = self.head
        string = ""
        while node:
            string += f"<{node.data}> "
            node = node.next
        return string
        

if(__name__ == "__main__"):
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(f"Queue: {q} : {q.length}")
    print(q.get())  
    print(f"Queue: {q} : {q.length}")
    print(q.get())  
    print(q.get())  
    print(f"Queue: {q} : {q.length}")

