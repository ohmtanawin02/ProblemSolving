ListA = [8, 12, 24, 3, 16, 10, 41]
ListB = ['C', 'B', 'F', 'Y', 'Z', 'G']
ListC = []
ChageListB = [ord(x) for x in ListB]
print(sum(ListA))
print(sum(ChageListB))
ListC = map(sum, zip(ListA, ChageListB))
print(ListC)
