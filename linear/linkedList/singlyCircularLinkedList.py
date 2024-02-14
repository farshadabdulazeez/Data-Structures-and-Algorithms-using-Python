class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
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
                self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == data:
                    prev.next = temp.next
                    temp = temp.next
                    break

    def display(self):
        if not self.head:
            print("List is empty!")
            return

        temp = self.head
        while True:
            print(temp.data, "--->", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("")

# Example usage for Singly Circular Linked List
scll = SinglyCircularLinkedList()
scll.append(1)
scll.append(2)
scll.append(3)
scll.prepend(0)

scll.display()  # Output: 0 ---> 1 ---> 2 ---> 3 --->

scll.delete_node(2)
scll.display()  # Output: 0 ---> 1 ---> 3 --->

