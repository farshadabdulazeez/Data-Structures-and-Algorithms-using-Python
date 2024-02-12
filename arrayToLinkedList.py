class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Append a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, data, position):
        """Insert a new node with the given data at the specified position in the linked list."""
        new_node = Node(data)
        if position == 0:
            # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            # Traverse to the specified position
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("Invalid position. Inserting at the end.")
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def delete_first(self):
        """Delete the first node in the linked list."""
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            print("Linked List is empty. Nothing to delete.")

    def display(self):
        """Display the linked list."""
        if self.head is None:
            print("Linked List is EMPTY.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

# Create a SingleLinkedList object
singly_linked_list = SingleLinkedList()

# Append elements to the linked list
array = [1, 2, 3, 4, 5]
for item in array:
    singly_linked_list.append(item)

# Display the initial linked list
print("Initial Linked List:")
singly_linked_list.display()

# Insert an element at position 2
singly_linked_list.insert(6, 2)
print("\nLinked List after inserting 6 at position 2:")
singly_linked_list.display()

# Delete the first element
singly_linked_list.delete_first()
print("\nLinked List after deleting the first element:")
singly_linked_list.display()
