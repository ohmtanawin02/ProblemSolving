ListA = [8, 12, 24, 3, 16, 10, 41]
ListB = ['C', 'B', 'F','K', 'Y', 'Z', 'G']
ListC = []
ChangeListB = [ord(x) for x in ListB]
print("Print List C :", ListC)
print("Print sum of List A : ", sum(ListA))
print("Print sum of List B : ", sum(ChangeListB))
ListC = [x + y for x, y in zip(ListA, ChangeListB)]
print("Print sum of List C : ", sum(ListC))
print(ListA)
print(ChangeListB)
print(ListC)
