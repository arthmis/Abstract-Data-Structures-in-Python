class Node:
    def __init__(self, item):
        self.data = item
        self.next_node = None

class Queue:
    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__tail.next_node = self.__head
        self.__head.next_node = self.__tail

    def enqueue(self, item):
        new_node = Node(item)
        new_node.next_node = self.__tail
        self.__tail.next_node.next_node = new_node
        self.__tail.next_node = new_node

    def dequeue(self):
        node_to_remove = self.__head.next_node
        self.__head.next_node = node_to_remove.next_node
        node_to_remove.next_node = None
        return node_to_remove.data

    def isEmpty(self):
        return self.__tail.next_node is self.__head

    def printQueue(self):
        iterator = self.__head.next_node
        while(iterator != self.__tail):
            print(iterator.data)
            iterator = iterator.next_node
