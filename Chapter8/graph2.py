import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node('A',)
G.add_edge('B', 'D')

nx.draw(G, with_labels=True, font_color='yellow', node_size=2000)
plt.show()
