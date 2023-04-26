

class Tree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.parent = None
            self.right = None
            self.left = None

    def __init__(self):
        self.head = None

    def createnode(self, key):
        n = self.Node(key)
        return n

    def insert(self, key):
        n = self.createnode(key)

        if self.head is None:
            self.head = n
            return

        temp = self.head

        while True:
            if key<temp.key:
                if temp.left is None:
                    temp.left = n
                    n.parent = temp
                    break

                temp = temp.left
            elif key>temp.key:
                if temp.right is None:
                    #do something
                    temp.right = n
                    n.parent = temp
                    break

                temp = temp.right

    def getHeight(self, root):
        if root is None:
            return -1

        leftheight = self.getHeight(root.left)
        rightheight = self.getHeight(root.right)

        return 1+max(leftheight, rightheight)

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self, root):
        if root is None:
            print("( ) ", end='')
            return
        print("( {} ".format(root.key), end='')
        self.printTree(root.left)
        self.printTree(root.right)
        print(") ", end='')
        

root = Tree()
root.insert(6)
root.insert(7)
root.insert(5)
root.insert(8)
root.insert(1)
root.printTree(root.head)
print()
print(root.getBalance(root.head))
# print(root.head.right.parent.left.key)

    

    
