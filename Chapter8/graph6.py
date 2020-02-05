import networkx as nx
import matplotlib.pyplot as plot

G = nx.Graph()

G.add_edge('man', 'baby', weight=1)
G.add_edge('baby', 'women', weight=0.5)
G.add_edge('man', 'women', weight=0.3)
G.add_edge('women', 'year', weight=1)
G.add_edge('year', 'man', weight=1)

final_avg = 999999999.99
final_key = ''

node_allSP = dict(nx.shortest_path_length(G, weight='weight'))
print(node_allSP)
for key in node_allSP:
    avg_nodeSP = sum(node_allSP[key].values())/(len(node_allSP[key]) - 1)
    print('AverageSP to all nodes of :', key, ' is ', avg_nodeSP)
    if final_avg > avg_nodeSP:
        final_avg = avg_nodeSP
        final_key = key

print('The centroid is : ', final_key, 'the length is ', final_avg)

edge_labels = nx.get_edge_attributes(G, 'weight')
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=2000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plot.show()
