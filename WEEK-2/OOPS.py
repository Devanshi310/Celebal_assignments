class Node:
    """A class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A class to manage the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node: {data}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added node: {data}")

    def print_list(self):
        """Print all elements in the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node from the list (1-based index)."""
        try:
            if n <= 0:
                raise IndexError("Index should be a positive integer.")

            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position {n} with data: {deleted_data}")
                return

            current = self.head
            for i in range(n - 2):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node at position {n} with data: {deleted_data}")
        except Exception as e:
            print("Error:", e)


# --- Testing the Implementation ---
if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    # Print the list
    ll.print_list()

    # Delete the 3rd node
    ll.delete_nth_node(3)
    ll.print_list()

    # Attempt to delete a node out of range
    ll.delete_nth_node(10)

    # Attempt to delete from an empty list
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)
