class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_middle(self):
        if not self.head or not self.head.next:
            print("LinkedList is empty or has only one element!")
            return

        prev = None
        slow = self.head
        fast = self.head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        slow.next = None

    def delete_begin(self):
        if not self.head:
            print("LinkedList is empty!")
        else:
            self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("LinkedList is empty!")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            self.head.next = self.head
            
    def insert_before(self, data, value):
        if not self.head:
            print("LinkedList is empty!")
            return
        new_node = Node(value)
        if self.head.data == data:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == data:
                    break
                temp = temp.next
            if not temp.next:
                print('Node not found')
            else:
                new_node.next = temp.next
                temp.next = new_node

    def insert_after(self, data, value):
        if not self.head:
            print("LinkedList is empty!")
            return
        new_node = Node(value)
        temp = self.head
        while temp:
            if temp.data == data:
                break
            temp = temp.next
        if not temp:
            print("Node not found")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def delete_element(self, value):
        if not self.head:
            print("LinkedList is empty!")
            return
        if self.head.data == value:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == value:
                    break
                temp = temp.next
            if not temp.next:
                print("Node not found")
            else:
                temp.next = temp.next.next

    def delete_and_find(self):
        if not self.head or not self.head.next:
            return None
        prev = None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def display(self):
        if not self.head:
            print("LinkedList is empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end=" ")
                temp = temp.next
                
                
ll = LinkedList()
ll.append(12)
ll.append(16)
ll.append(20)
ll.prepend(10)
ll.prepend(8)
ll.prepend(4)

# ll.delete_and_find()
print(ll.delete_and_find())
# ll.delete_element(0)
ll.insert_before(12, 12)
# ll.insert_after(10, 22)
# ll.delete_begin()
ll.delete_middle()
# ll.delete_end()
ll.display()
