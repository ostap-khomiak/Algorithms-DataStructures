
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    

    def pop(self):
        if not self.head:
            return None
        h = self.head
        self.head = h.prev
        h.prev = None   # removing the reference to the previous node
        self.length = max(0, self.length - 1)  # never go negative
        return h.data

    
    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.prev = self.head
            self.head = new_node
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
            node = node.prev
        return string


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack: {s} | Length: {s.length}")
    print(f"Peek: {s.peek()}")
    print(f"Popping: {s.pop()}")  
    print("Pushing 4")
    s.push(4)
    print(f"Stack: {s} | Length: {s.length}")
    print(f"Popping: {s.pop()}")  
    print(f"Popping: {s.pop()}")  
    print(f"Stack: {s} | Length: {s.length}")
    print(f"Popping: {s.pop()}")  
    print(f"Popping: {s.pop()}")  
