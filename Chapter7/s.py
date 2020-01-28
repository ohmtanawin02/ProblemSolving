if root == None:
            return None
        if root.left == None and root.right == None:
            if root.key == key:
                return None
            else:
                return root


                return root
        if key < root.key:
            root.left = Delete(root.left, key)
        elif key > root.key:
            root.right = Delete(root.right, key)
        else:
            if root.left is None:
                num = root.right
                root = None
                return num
            elif root.right is None:
                num = root.left
                root = None
                return num