class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            temp = self.head.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            temp = self.head.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, data):
        if not self.head:
            print("List is empty!")
            return

        if self.head.data == data:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            if self.head.next == self.head:
                self.head = None
            else:
                temp.next = self.head.next
                self.head.next.prev = temp
                self.head = self.head.next
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                if temp.data == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break

    def display_forward(self):
        if not self.head:
            print("List is empty!")
            return

        temp = self.head
        while True:
            print(temp.data, "<-->", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("")

    def display_backward(self):
        if not self.head:
            print("List is empty!")
            return

        temp = self.head.prev
        while True:
            print(temp.data, "<-->", end=" ")
            temp = temp.prev
            if temp == self.head.prev:
                break
        print("")

# Example usage for Doubly Circular Linked List
dcll = DoublyCircularLinkedList()
dcll.append(1)
dcll.append(2)
dcll.append(3)
dcll.prepend(0)

dcll.display_forward()  # Output: 0 <--> 1 <--> 2 <--> 3 <-->

dcll.delete_node(2)
dcll.display_forward()  # Output: 0 <--> 1 <--> 3 <-->
dcll.display_backward() # Output: 3 <--> 1 <--> 0 <-->
