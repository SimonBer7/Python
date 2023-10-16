class Node:
    """
    The `Node` class represents a single element in a singly linked list.

    Attributes:
        info: The data stored in the node.
        next: Reference to the next node in the linked list.

    Methods:
        - `__init__(self, info)`: Initializes a new node with the provided data.
    """

    def __init__(self, info):
        """
        Initializes a new node with the given data.

        Args:
            info: The data to be stored in the node.
        """
        self.info = info
        self.next = None


class MyLinkedList:
    """
    The `MyLinkedList` class represents a singly linked list data structure.

    Attributes:
        beginning: Reference to the first node in the linked list.

    Methods:
        - `__init__(self)`: Initializes an empty linked list.
        - `add(self, data)`: Adds a new node with the provided data to the end of the list.
        - `select(self)`: Traverses the linked list and prints the data of each node.

    Usage:
    ```python
    single_linked_list = MyLinkedList()

    single_linked_list.add(9)
    single_linked_list.add(17)
    single_linked_list.add(11)
    single_linked_list.add(18)
    single_linked_list.add(6)

    single_linked_list.select()
    ```
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.beginning = None

    def add(self, data):
        """
        Adds a new node with the provided data to the end of the linked list.

        Args:
            data: The data to be added to the linked list.
        """
        new_node = Node(data)
        if self.beginning is None:
            self.beginning = new_node
        else:
            current = self.beginning
            while current.next is not None:
                current = current.next
            current.next = new_node

    def select(self):
        """
        Traverses the linked list and prints the data of each node.
        """
        current = self.beginning
        while current is not None:
            print(current.info)
            current = current.next
