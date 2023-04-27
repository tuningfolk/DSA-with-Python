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

        #balancing
        temp1 = n
        temp2 = n.parent
        if temp2 is None:
            return
        temp3 = temp2.parent

        while temp3 is not None:
            if self.getBalance(temp3) == -2:

                #RL case
                if temp1 is not temp2.right:
                    self.rightrotate(temp2) #now temp2 is the right child of temp1
                    
                    #fixing it (making it as if it was RR in the first place)
                    temp2 = temp1
                    temp1 = temp2.right

                self.leftrotate(temp3)
                temp3 = temp2.parent

            elif self.getBalance(temp3) == 2:

                if temp1 is not temp2.left:
                    self.leftrotate(temp2)

                    temp2 = temp1
                    temp1 = temp2.left

                self.rightrotate(temp3)
                temp3 = temp3.parent

            else:
                temp3 = temp3.parent
                temp2 = temp2.parent
                temp1 = temp1.parent

                    


    def leftrotate(self, root):
        r  = root.right
        p = root.parent

        #transferring the right left child (to the other side)
        if r.left is not None:
            root.right = r.left
            r.left.parent = root
        else:
            root.right = None

        #updating the parent of the right child
        if p is not None:
            if p.right is root:
                p.right = r
            else:
                p.left = r
            
            r.parent = p
        else:
            self.head = r
            r.parent = None

        #making the rotation
        r.left = root
        root.parent = r

    def rightrotate(self, root):
        p = root.parent
        l = root.left

        #transferring the left-right child (to the other side)
        if l.right is not None:
            root.left = l.right
            l.right.parent = root
        else:
            root.left = None

        #updating the parent of the left child
        if p is not None:
            if p.right == root:
                p.right = l
            else:
                p.left = l

            l.parent = p
        else:
            self.head = l
            l.parent = None

        #making the rotation
        l.right = root
        root.parent = l
    def findNode(self, root,value):
        if root.key == value:
            return root
        
        if value<root.key:
            return self.findNode(root.left, value)
        else:
            return self.findNode(root.right, value)
    def delete(self, root):
        r = root.right
        l = root.left

        if r is not None:
            temp = r
            #going to the left most node of the right sub tree
            while temp.left is not None:
                temp = temp.left

            #changing the value of the to-be deleted node
            root.key = temp.key

            if temp is r:
                #right child has no left subtree
                r.left = root.left
                p = root.parent
                if p is None:
                    self.head = r
                    r.parent = None
                elif p.right == root:
                    p.right = r
                    r.parent = p
                else:
                    p.left = r
                    r.parent = p

                temp1 = r #saving into temp for later use (rotation)
                # del root
                
            else:    
                p = temp.parent
                p.left = temp.right
                if temp.right is not None:
                    temp.right.parent = p
                
                temp1 = temp.right #saving into temp for later use
            
        elif l is not None:
            temp = l
            while temp.right is not None:
                temp = temp.right

            root.key = temp.key
            if temp is l:
                l.right = root.right
                p = root.parent
                if p is None:
                    self.head = l
                    l.parent = None
                elif p.right == root:
                    p.right = l
                    l.parent = p
                else:
                    p.left = l
                    l.parent = p

                temp1 = l #saving the new node into temp for later use(rotation)
                # del root
            else:
                p = temp.parent
                p.right = temp.left
                
                if temp.left is not None:
                    temp.left.parent = p
                temp1 = temp.left #saving into temp for later use

        else:
            #no child (leaf node)
            if root is self.head:
                del root
                self.head = None
                return
            
            if root is root.parent.left:
                root.parent.left = None
            else:
                root.parent.right = None
            
            temp1 = root #saving for later use

    
        #now rotation part
        # temp1 = temp.parent
        balance = self.getBalance(temp1)
        while temp1 is not None:
            balance = self.getBalance(temp1)
            # print(balance)
            # print(temp1.key, balance)
            if balance > 1 or balance < -1:
                if balance > 1: #larger left subtree
                    temp2 = temp1.left
                    balance2 = self.getBalance(temp2)

                    if balance2 == 0 or balance2 == 1:
                        #LL case
                        temp3 = temp2.left

                        self.rightrotate(temp1)
                        temp1 = temp2.parent
                    else:
                        #LR case
                        temp3 = temp2.right

                        self.leftrotate(temp2)
                        temp3 = temp2
                        temp2 = temp2.parent

                        self.rightrotate(temp1)
                        temp1 = temp2.parent
                else:
                    #Larger right subtree
                    temp2 = temp1.right

                    balance = self.getBalance(temp2)

                    if balance == 0 or balance == -1:
                        ##RR case
                        temp3 = temp2.right

                        self.leftrotate(temp1)
                        temp1 = temp2.parent
                    else:
                        #RL case
                        temp3 = temp2.left

                        self.rightrotate(temp2)
                        temp3 = temp2
                        temp2 = temp2.parent

                        self.leftrotate(temp1)
                        temp1 = temp2.parent
            else:
                temp1 = temp1.parent

        

    def getHeight(self, root):
        if root is None:
            return -1

        leftheight = self.getHeight(root.left)
        rightheight = self.getHeight(root.right)

        return 1+max(leftheight, rightheight)

    def getBalance(self, root):
        if root is None:
            return 0
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
root.insert(4)
root.insert(8)
root.insert(5)
root.insert(7)
root.insert(2)
root.insert(10)
root.insert(1)
root.insert(3)
root.insert(9)
root.insert(11)
root.printTree(root.head)
print()
root.delete(root.findNode(root.head,4))
# root.insert(9)
root.printTree(root.head)
print()
# root.rightrotate(root.head)
# root.printTree(root.head)
# print()
# print(root.head.right.parent.left.key)

    

    
