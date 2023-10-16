class Node:
    """
    The `Node` class represents a single element in a doubly linked list.

    Attributes:
        info: The data stored in the node.
        next: Reference to the next node in the linked list.
        previous: Reference to the previous node in the linked list.

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
        self.previous = None


class MyDoubleLinkedList:
    """
    The `MyDoubleLinkedList` class represents a doubly linked list data structure.

    Attributes:
        beginning: Reference to the first node in the linked list.
        last: Reference to the last node in the linked list.

    Methods:
        - `__init__(self)`: Initializes an empty doubly linked list.
        - `add(self, data)`: Adds a new node with the provided data to the end of the list.
        - `select_first(self)`: Traverses the linked list from the first node and prints the data of each node.
        - `select_last(self)`: Traverses the linked list from the last node and prints the data of each node.

    Usage:
    ```python
    double_linked_list = MyDoubleLinkedList()

    double_linked_list.add(11)
    double_linked_list.add(18)
    double_linked_list.add(9)
    double_linked_list.add(6)
    double_linked_list.add(39)

    double_linked_list.select_first()
    print("----------")
    double_linked_list.select_last()
    ```
    """

    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.beginning = None
        self.last = None

    def add(self, data):
        """
        Adds a new node with the provided data to the end of the doubly linked list.

        Args:
            data: The data to be added to the linked list.
        """
        new_node = Node(data)
        if self.beginning is None:
            self.beginning = new_node
            self.last = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node

    def select_first(self):
        """
        Traverses the doubly linked list from the first node and prints the data of each node.
        """
        current = self.beginning
        while current is not None:
            print(current.info)
            current = current.next

    def select_last(self):
        """
        Traverses the doubly linked list from the last node and prints the data of each node.
        """
        current = self.last
        while current is not None:
            print(current.info)
            current = current.previous
