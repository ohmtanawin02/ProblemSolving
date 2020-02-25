import matplotlib.pyplot as plt
import networkx as nx
import string

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'K'), ('B', 'G'),
                  ('K', 'G'), ('K', 'C'), ('K', 'B'), ('B', 'H'), ('B', 'K'),
                  ('C', 'K'), ('C', 'A'), ('D', 'A'), ('D', 'E'), ('E', 'H'),
                  ('E', 'Z'), ('F', 'H'), ('F', 'J'), ('H', 'F'), ('H', 'E'),
                  ('J', 'F'), ('J', 'H'), ('J', 'Z'), ('Z', 'E'), ('Z', 'J'),
                  ('B', 'A')])
add = input("Input :")

result = []
for i in G.neighbors(add):
    for n in G.neighbors(i):
        if n == add:
            del n
        else:
            result.append(n)
result = list(set(result))
print(result)


nx.draw(G, with_labels=True, font_color='yellow', node_size=1500)
plt.show()
