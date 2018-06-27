class Node:
    def __init__(self, item):
        self.data = item
        self.previous_node = None
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__head.next_node = self.__tail
        self.__tail.previous_node = self.__head

    def insertFront(self, item):
        new_item = Node(item)
        new_item.next_node = self.__head.next_node
        self.__head.next_node.previous_node = new_item
        self.__head.next_node = new_item
        new_item.previous_node = self.__head

    def insertBack(self, item):
        new_item = Node(item)
        new_item.previous_node = self.__tail.previous_node
        self.__tail.previous_node.next_node = new_item
        self.__tail.previous_node = new_item
        new_item.next_node = self.__tail

    def removeFront(self):
        if self.__head.next_node is self.__tail:
            return None
        else:
            item_to_remove = self.__head.next_node.data
            self.__head.next_node.next_node.previous_node = self.__head
            self.__head.next_node = self.__head.next_node.next_node
            return item_to_remove

    def removeBack(self):
        if self.__tail.previous_node is self.__head:
            return None
        else:
            item_to_remove = self.__tail.previous_node.data
            self.__tail.previous_node.previous_node.next_node = self.__tail
            self.__tail.previous_node = self.__tail.previous_node.previous_node
            return item_to_remove

    def find(self, item):
        if(self.__head.next_node is self.__tail):
            return False
        else:
            iterator = self.__head.next_node
            while iterator.next_node is not None:
                if(item == iterator.data):
                    return True
                iterator = iterator.next_node

            return False

    def printList(self):
        iterator = self.__head.next_node
        while(iterator.next_node is not None):
            print(iterator.data)
            iterator = iterator.next_node
