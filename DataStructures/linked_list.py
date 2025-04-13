
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    # Doubly-linked list

    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        node = self.head

        counter = 0

        while node != None:
            counter += 1
            node = node.next

        return counter

    def insertAt(self, data, index):
        node = self.head
        counter = 0
        new_node = Node(data)

        while counter != index:
            if node is None: 
                return False
            node = node.next
            counter += 1
        
        if node == self.head:
            self.head = new_node
        else:
            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
        return True


        

    def remove(self, data):
        node = self.head
        
        while node.data != data:
            if node is None:
                return False
            node = node.next
        
        if node == self.head:  
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:  
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:  
                self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return True

    def removeAt(self, index):
        node = self.head
        counter = 0

        while counter != index:
            if node is None: 
                return False
            node = node.next
            counter += 1

        if node == self.head:  
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:  
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:  
                self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return True
        

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            

    def pop(self):
        if not self.tail:
            return None
        
        popped_node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return popped_node.data

    

    def get(self, index):
        node = self.head
        
        counter = 0
        while counter != index:
            if node is None:
                return "No such node"
            node = node.next
            counter += 1

        return node.data
            



    def __str__(self):
        string = ""
        node = self.head
        while node is not None:
            string += f"<{node.data}> "
            node = node.next

        return string
    



if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(10)

    print(f"Linked list: {linked_list}")
    print(f"Linked List length: {linked_list.length()}")

    print(f"Get 1: {linked_list.get(1)}")
    print(f"Get 5: {linked_list.get(5)}")
    print("-" * 30)
    print(f"Linked list: {linked_list}")
    print(f"Inserting At 1: {linked_list.insertAt(25, 1)}")
    print(f"Linked list: {linked_list}")
    print(f"Pop: {linked_list.pop()}")
    print(f"Linked list: {linked_list}")
    print(f"Appending 30: {linked_list.append(30)}")
    print("-" * 30)
    print(f"Linked list: {linked_list}")
    print(f"Removing At 1: {linked_list.removeAt(1)}")
    print(f"Linked list: {linked_list}")
    print(f"Removing At 5: {linked_list.removeAt(5)}")
    print(f"Linked list: {linked_list}")
    print(f"Removing 30: {linked_list.remove(30)}")
    print(f"Linked list: {linked_list}")
    print(f"Removing At 0: {linked_list.removeAt(0)}")
    print(f"Linked list: {linked_list}")



