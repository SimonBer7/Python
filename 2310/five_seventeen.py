class Node:
    def __init__(self, data):
        """
        Initializes an instance of the Node class, representing a node in a linked list.

        :param data: Data to be stored in the node.
        """
        self.data = data
        self.next = None
        self.previous = None

class MyQueue:
    def __init__(self):
        """
        Initializes an instance of the MyQueue class, which represents a queue implemented using a linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def count(self):
        """
        Returns the number of elements in the queue.

        :return: The number of elements in the queue.
        """
        return self.size

    def clear(self):
        """
        Empties the queue by setting the head and tail to None and size to 0.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        """
        Adds a new node with the given data to the end of the queue.

        :param data: Data to be stored in the new node.
        """
        temp = Node(data)

        if self.head is None and self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            temp.previous = self.tail
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def pop_node(self):
        """
        Removes and returns the first node from the queue.

        :return: Data of the first node in the queue.
        :raises: ValueError if the queue is empty.
        """
        if self.size == 0:
            raise ValueError("Nothing to pop.")

        first_node = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = first_node.next
            self.tail.previous = None
        self.size -= 1
        return first_node.data

    def pop_all_nodes(self):
        """
        Removes and returns all nodes from the queue as a list.

        :return: A list containing the data of all nodes in the queue.
        """
        nodes = []
        while self.size > 0:
            nodes.append(self.pop_node())
        return nodes

    def print(self):
        """
        Creates a text string representing the content of the queue.

        :return: A text string describing the content of the queue.
        """
        text = ""
        if self.count() != 0:
            temp = self.head
            while temp.next is not None:
                text += str(temp.data) + ", "
                temp = temp.next
            text += str(temp.data)
        else:
            text += "Queue is empty."
        return text


    def __len__(self):
        return self.size


    def __getitem__(self, item):
        if item < 0 or item >= self.size:
            raise IndexError("Error, index out of range")

        current = self.head
        for i in range(item):
            current = current.next

        return current.data

    def __setitem__(self, key, value):
         if key < 0 or key >= self.size:
            raise IndexError("Error, index out of range")
         else:
            current = self.head
            for i in range(key):
                current = current.next

            current.data = value

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False



# Testing
queue = MyQueue()

queue.add_node(5)
queue.add_node(6)
queue.add_node(7)
queue.add_node(8)
print("Queue: " + str(queue.print()))
print(queue[3])
queue[0] = "Pepa"
print("Queue: " + str(queue.print()))
if "Pepa" in queue:
    print("Pepa je v seznamu")
print("Count of nodes in queue: " + str(queue.count()))
print("Second count using len(): "+str(len(queue)))
print("Popped: " + str(queue.pop_node()))
print("Queue: " + str(queue.print()))
print("Popped all nodes: " + str(queue.pop_all_nodes()))
print("Queue: " + str(queue.print()))
queue.add_node(11)
queue.add_node(19)
print("Queue: " + str(queue.print()))
queue.clear()
print("Queue: " + str(queue.print()))
