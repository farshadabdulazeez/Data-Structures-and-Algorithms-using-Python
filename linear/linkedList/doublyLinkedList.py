class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True  # Node found and deleted
            current = current.next
        return False  # Node not found

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return True  # Node inserted after the target node
            current = current.next
        return False  # Target node not found

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, "<-->", end=" ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, "<-->", end=" ")
            current = current.prev
        print("None")

    def reverse(self):
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)

dll.display_forward()  # Output: 0 <--> 1 <--> 2 <--> 3 <--> None
dll.display_backward()  # Output: 3 <--> 2 <--> 1 <--> 0 <--> None

dll.insert_after(1, 1.5)
dll.display_forward()  # Output: 0 <--> 1 <--> 1.5 <--> 2 <--> 3 <--> None

dll.delete_node(2)
dll.display_forward()  # Output: 0 <--> 1 <--> 1.5 <--> 3 <--> None

dll.reverse()
dll.display_forward()  # Output: 3 <--> 1.5 <--> 1 <--> 0 <--> None
