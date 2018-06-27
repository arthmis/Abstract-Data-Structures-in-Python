class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.__root = None


    def isEmpty(self):
        return self.innerIsEmpty(self.__root)


    def innerIsEmpty(self, tree_root):
        return tree_root is None


    def insert(self, item):
        self.__root = self.innerInsert(self.__root, item)
        self.__root = self.balance(self.__root)


    def innerInsert(self, tree_root, item):
        if tree_root is None:
            new_leaf = Node(item)
            return new_leaf
        elif item < tree_root.data:
            tree_root.left = self.innerInsert(tree_root.left, item)
        elif item > tree_root.data:
            tree_root.right = self.innerInsert(tree_root.right, item)
        tree_root = self.balance(tree_root)
        return tree_root


    def delete(self, item):
        self.__root = self.innerDelete(self.__root, item)


    def innerDelete(self, tree_root, item):
        if tree_root is None:
            return
        elif item < tree_root.data:
            tree_root.left = self.innerDelete(tree_root.left, item)
        elif item > tree_root.data:
            tree_root.right = self.innerDelete(tree_root.right, item)
        else:
            if tree_root.left is None and tree_root.right is None:
                tree_root = None
            elif tree_root.right is None and tree_root.left is not None:
                tree_root.data = tree_root.left.data
                tree_root.left = tree_root.left.left
                tree_root.right = tree_root.left.right
            elif tree_root.left is None and tree_root.right is not None:
                tree_root.data = tree_root.right.data
                tree_root.left = tree_root.right.left
                tree_root.right = tree_root.right.right
            else:
                tree_root.data = self.innerFindMin(tree_root.right)
                tree_root.right = self.innerDelete(tree_root.right, tree_root.data)
        tree_root = self.balance(tree_root)
        return tree_root


    def find(self, item):
        return self.innerFind(self.__root, item)


    def innerFind(self, tree_root, item):
        if tree_root is None:
            return False
        elif item < tree_root.data:
            return self.innerFind(tree_root.left, item)
        elif item > tree_root.data:
            return self.innerFind(tree_root.right, item)
        return True


    def findMin(self):
        return self.innerFindMin(self.__root)


    def innerFindMin(self, tree_root):
        if tree_root is None:
            return None
        if tree_root.left is None:
            return tree_root.data
        else:
            return self.innerFindMin(tree_root.left)


    def findMax(self):
        return self.innerFindMax(self.__root)


    def innerFindMax(self, tree_root):
        if tree_root is None:
            return None
        if tree_root.right is None:
            return tree_root.data
        else:
            return self.innerFindMax(tree_root.right)


    def inOrderTraversal(self):
        self.innerInOrderTraversal(self.__root)


    def innerInOrderTraversal(self, tree_root):
        if self.isEmpty():
            print("tree is empty\n")
            return
        if tree_root is None:
            return
        self.innerInOrderTraversal(tree_root.left)
        print(tree_root.data)
        self.innerInOrderTraversal(tree_root.right)


    def preOrderTraversal(self):
        self.innerPreOrderTraversal(self.__root)


    def innerPreOrderTraversal(self, tree_root):
        if self.isEmpty():
            print("tree is empty\n")
            return
        if tree_root is None:
            return
        print(tree_root.data)
        self.innerPreOrderTraversal(tree_root.left)
        self.innerPreOrderTraversal(tree_root.right)


    def balance(self, tree_root):
        if tree_root is None:
            return
        left_height = self.height(tree_root.left)
        right_height = self.height(tree_root.right)
        if left_height - right_height > 1:
            if self.height(tree_root.left.left) >= \
               self.height(tree_root.left.right):
                tree_root = self.rightRotate(tree_root)
            else:
                tree_root = self.doubleRotateWithLeftChild(tree_root)
        elif right_height - left_height > 1:
            if self.height(tree_root.right.right) >= \
               self.height(tree_root.right.left):
                tree_root = self.leftRotate(tree_root)
            else:
                tree_root = self.doubleRotatewithRightChild(tree_root)
        temp_root = tree_root
        tree_root.height = max(self.height(tree_root.right),
                               self.height(tree_root.left)) + 1
        return tree_root


    def leftRotate(self, tree_root):
        right_child = tree_root.right
        tree_root.right = right_child.left
        right_child.left = tree_root
        tree_root.height = max(self.height(tree_root.left),
                               self.height(tree_root.right)) + 1
        right_child.height = max(self.height(right_child.left),
                                self.height(right_child.right)) + 1
        return right_child


    def doubleRotateWithLeftChild(self, tree_root):
        tree_root.left = self.leftRotate(tree_root.left)
        tree_root = self.rightRotate(tree_root)
        return tree_root


    def rightRotate(self, tree_root):
        left_child = tree_root.left
        tree_root.left = left_child.right
        left_child.right = tree_root
        tree_root.height = max(self.height(tree_root.left),
                               self.height(tree_root.right)) + 1
        left_child.height = max(self.height(left_child.left),
                                self.height(left_child.right)) + 1
        return left_child


    def doubleRotatewithRightChild(self, tree_root):
        tree_root.right = self.rightRotate(tree_root.right)
        tree_root = self.leftRotate(tree_root)
        return tree_root


    def height(self, tree_root):
        if tree_root is None:
            return -1
        else:
            return tree_root.height
