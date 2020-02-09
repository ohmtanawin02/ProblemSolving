import networkx as nx
import matplotlib.pylab as plt

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'M'), ('A', 'L'), ('B', 'C'), ('B', 'D'),
                  ('B', 'N'), ('B', 'O'), ('C', 'D'), ('D', 'E'), ('D', 'O'),
                  ('E', 'F'), ('F', 'G'), ('F', 'N'), ('G', 'H'), ('H', 'N'),
                  ('H', 'I'), ('H', 'P'), ('P', 'O'), ('P', 'I'), ('P', 'M'),
                  ('I', 'J'), ('J', 'K'), ('K', 'M'), ('K', 'L'), ])

Alist = nx.all_neighbors(G, 'A')
Elist = nx.all_neighbors(G, 'B')
Ilist = nx.all_neighbors(G, 'C')

A = []
B = []
C = []

for a in Alist:
    A.append(a)
    for n in nx.all_neighbors(G, a):
        A.append(n)

for b in Elist:
    B.append(b)
    for m in nx.all_neighbors(G, b):
        B.append(m)

for c in Ilist:
    C.append(C)
    for j in nx.all_neighbors(G, c):
        C.append(j)

for q in A:
    for k in B:
        for p in C:
            if q == k == p:
                print(q)
print(A)
print(B)
print(C)
