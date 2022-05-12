from Node import Node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail
        self.__size = 0

    def __repr__(self):
        nodes = []
        current_node = self.__head
        while current_node is not None:
            nodes.append(str(current_node.element))
            current_node = current_node.next
        if self.__size == 0:
            return "LinkedList is empty."
        return "Head-> " + " -> ".join(nodes) + " <-Tail"

    def add_first(self, e):
        new_node = Node(e)
        new_node.next = self.__head
        self.__head = new_node   # head is now the new node, you can think of as a kind of pointer.
        self.__size += 1
        if self.__tail is None:  # this is true if the new node is the only node in the L-L.
            self.__tail = self.__head

    def add_last(self, e):
        new_node = Node(e)
        if self.__tail is None:  # the only node in list.
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def insert(self, e, *, index):
        if index == 0:
            self.add_first(e)
        elif index >= self.__size:
            self.add_last(e)
        else:
            current_node = self.__head
            for _ in range(index-1):
                current_node = current_node.next
            temp = current_node.next
            current_node.next = Node(e)
            current_node.next.next = temp
            self.__size += 1

    def remove_first(self):
        if self.__size == 0:
            return None
        else:
            deleted_node = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            if self.__head is None:  # if there is only one node, then next=None, i.e. this is one node case.
                self.__tail = None
            return deleted_node.element

    def remove_last(self):
        if self.__size == 0:
            return None
        else:
            current_node = self.__head
            for _ in range(self.__size - 2):
                current_node = current_node.next
            self.__tail = current_node
            self.__tail.next = None
            self.__size -= 1

            if self.__size == 0:
                self.__head = None
                self.__tail = None

    def remove_at(self, index):
        if index < 0 or index >= self.__size:
            return None
        elif index == 0:
            return self.remove_first()
        elif index == self.__size - 1:
            return self.remove_last()
        else:
            previous_node = self.__head
            for _ in range(index - 1):  # iteration up to the previous node.
                previous_node = previous_node.next
            current_node = previous_node.next
            previous_node.next = current_node.next
            self.__size -= 1
            return current_node.element
