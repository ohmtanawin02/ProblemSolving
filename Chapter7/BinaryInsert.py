class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def findval(self, data):
        if data < self.data:
            if self.left is None:
                return str(data)+" Not Found"
            return self.left.findval(data)
        elif data > self.data:
            if self.right is None:
                return str(data)+" Not Found"
            return self.right.findval(data)
        else:
            print(str(self.data) + " is found")

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def DeleteBinary(self, root):
        if self.root is None:
            if root < self.root:
                if self.left is None:
                    self.left = DeleteBinary(self.left, root)
            elif root > self.root:
                if self.right is None:
                    self.right = DeleteBinary(self.left, root)
        else:
            self.root = data


root = Node(60)
root.insert(65)
root.insert(75)
root.insert(32)
root.insert(47)
root.insert(50)
root.insert(81)
root.insert(51)
root.insert(73)
root.findval(65)

print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
print(root.DeleteBinary(51))

# if root < self.data:
#self.left = DeleteBinary(self.left, root)
# elif root > self.data:
#self.right = DeleteBinary(self.right, root)
# else:
#print('dont delete')
