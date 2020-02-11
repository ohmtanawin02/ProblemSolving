import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'K'), ('B', 'G'),
                  ('B', 'H'), ('B', 'O'), ('C', 'K'), ('C', 'A'), ('D', 'A'),
                  ('D', 'E'), ('E', 'H'), ('E', 'Z'), ('F', 'H'), ('F', 'J'),
                  ('H', 'F'), ('H', 'E'), ('J', 'F'), ('J', 'H'), ('J', 'Z'),
                  ('Z', 'E'), ('Z', 'J')])

nx.draw(G, with_labels=True, font_color='yellow', node_size=1500)
plt.show()
