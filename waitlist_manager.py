# Create a Node class to represent each customer in the waitlist
class Node:
    """
    A node in a singly linked list.
    """

    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    """
    A singly linked list used to manage a customer waitlist.
    """

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head

        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"

            current = current.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input(
                "Enter customer name to add to front: "
            ).strip()

            waitlist.add_front(name)
            print(f"{name} added to the front of the waitlist")

        elif choice == "2":
            name = input(
                "Enter customer name to add to end: "
            ).strip()

            print(waitlist.add_end(name))

        elif choice == "3":
            name = input(
                "Enter customer name to remove: "
            ).strip()

            print(waitlist.remove(name))

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1–5.")


if __name__ == "__main__":
    waitlist_generator()


"""
DESIGN MEMO

My waitlist uses a singly linked list made from Node objects. Each Node stores a
customer's name and a next pointer that connects it to the following customer.
The LinkedList class manages those nodes. The add_front method creates a new
node, points it toward the current first node, and makes it the new head. The
add_end method follows the next pointers until it reaches the last node, then
connects that node to the new customer. The remove method searches through the
nodes by name. When it finds the correct customer, it changes a pointer so the
list skips over that node. The print_list method also follows the next pointers,
starting at the beginning and printing every customer in order.

The head is important because it stores the starting point of the entire list.
If the head is None, the waitlist is empty. Adding a VIP to the front requires
updating the new node's next pointer and changing the head. Removing the first
customer also requires moving the head to the second node. Without the head,
the program would have no way to reach the remaining customers.

A real engineer might use a custom linked structure when items must frequently
be inserted or removed without shifting every other item. Examples include
ticket queues, music playlists, browser navigation, and task schedulers. A
custom structure also allows an engineer to control exactly how priority
customers are added or how removals behave. For a larger ticketing system, I
would probably add a tail pointer so customers could be added to the end in
constant time. I would also assign customers unique IDs because different
customers may have the same name.
"""
