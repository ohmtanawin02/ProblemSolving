class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
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
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+"Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+"Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+" is Found")
    def inorderTraversal(self,root):
            res = []
            if root:
                res = self.inorderTraversal(root.left)
                res.append(root.data)
                res = res + self.inorderTraversal(root.right)
            return res
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    def PostorderTrraversal(self,root):
        res = []
        if root:
            res = self.PostorderTrraversal(root.left)
            res = res+self.PostorderTrraversal(root.right)
            res.append(root.data)
        return res
    def goinNode(self, node):
        deepgo = node
        while(deepgo.left is not None):
            deepgo = deepgo.left
        return deepgo
    def delete(self, data):
        if self is None:
            return None 
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                dataX = self.right
                self = None
                return dataX
            elif self.right is None:
                dataX = self.left
                self = None
                print(dataX)
                return dataX
            dataX = self.goinNode(self.right)
            self.data = dataX.data
            self.right = self.right.delete(dataX.data)

        return self
    
root = Node(100)
root.insert(50)
root.insert(60)
root.insert(30)
root.insert(150)
root.insert(120)
root.delete(150)
print(root.inorderTraversal(root))
#print(root.PreorderTraversal(root))
#print(root.PostorderTrraversal(root))
#for i in range(51):
    #root.insert(i)
root.PrintTree()
#print(root.findval(56))

