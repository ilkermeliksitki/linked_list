class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def __repr__(self):
        return "[element: " + str(self.element) + ", next: " + str(self.next) + "]"
