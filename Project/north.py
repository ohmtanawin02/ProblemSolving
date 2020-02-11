import networkx as nx
import matplotlib.pyplot as plot

G = nx.Graph()

G.add_edge('Chiang rai', 'Phayao', weight=94)
G.add_edge('Chiang rai', 'Chiang mai', weight=182)
G.add_edge('Chiang rai', 'Lampang', weight=225)
G.add_edge('Phayao', 'Chiang rai', weight=94)
G.add_edge('Phayao', 'Lampang', weight=131)
G.add_edge('Phayao', 'Nan', weight=176)
G.add_edge('Phayao', 'Phrae', weight=141)
G.add_edge('Mae Hong Son', 'Chiang mai', weight=349)
G.add_edge('Mae Hong Son', 'Tak', weight=499)
G.add_edge('Chiang mai', 'Chiang rai', weight=182)
G.add_edge('Chiang mai', 'Lampang', weight=92)
G.add_edge('Chiang mai', 'Lampoon', weight=21)
G.add_edge('Chiang mai', 'Tak', weight=265)
G.add_edge('Chiang mai', 'Mae Hong son', weight=349)
G.add_edge('Lampoon', 'Lampang', weight=71)
G.add_edge('Lampoon', 'Chiang mai', weight=21)
G.add_edge('Lampoon', 'Tak', weight=244)
G.add_edge('Lampang', 'Chiang rai', weight=97)
G.add_edge('Lampang', 'Chiang mai', weight=92)
G.add_edge('Lampang', 'Phayao', weight=131)
G.add_edge('Lampang', 'Phrae', weight=109)
G.add_edge('Lampang', 'Sukhothai', weight=207)
G.add_edge('Lampang', 'Tak', weight=174)
G.add_edge('Lampang', 'Lampoon', weight=71)
G.add_edge('Phrae', 'Phayao', weight=141)
G.add_edge('Phrae', 'Nan', weight=118)
G.add_edge('Phrae', 'Lampang', weight=109)
G.add_edge('Phrae', 'Uttaradit', weight=74)
G.add_edge('Phrae', 'Sukhothai', weight=165)
G.add_edge('Nan', 'Phrae', weight=118)
G.add_edge('Nan', 'Uttaradit', weight=191)
G.add_edge('Nan', 'Phayao', weight=118)
G.add_edge('Tak', 'Mae Hong son', weight=499)
G.add_edge('Tak', 'Chiang mai', weight=265)
G.add_edge('Tak', 'Lampoon', weight=244)
G.add_edge('Tak', 'Lampang', weight=174)
G.add_edge('Tak', 'Sukhothai', weight=79)
G.add_edge('Tak', 'Kamphaeng Phet', weight=68)
G.add_edge('Tak', 'Nakhonsawan', weight=185)
G.add_edge('Tak', 'Uthai Thani', weight=234)
G.add_edge('Sukhothai', 'Phrae', weight=165)
G.add_edge('Sukhothai', 'Uttaradit', weight=100)
G.add_edge('Sukhothai', 'Phitsanulok', weight=59)
G.add_edge('Sukhothai', 'Kamphaeng phet', weight=77)
G.add_edge('Sukhothai', 'Tak', weight=79)
G.add_edge('Sukhothai', 'Lampang', weight=207)
G.add_edge('Uttaradit', 'Phrae', weight=74)
G.add_edge('Uttaradit', 'Nan', weight=191)
G.add_edge('Uttaradit', 'Sukhothai', weight=100)
G.add_edge('Uttaradit', 'Phitsanulok', weight=118)
G.add_edge('Phitsanulok', 'Phetchabun', weight=170)
G.add_edge('Phitsanulok', 'Sukhothai', weight=59)
G.add_edge('Phitsanulok', 'Kamphaeng Phet', weight=103)
G.add_edge('Phitsanulok', 'Phichit', weight=73)
G.add_edge('Phitsanulok', 'Uttaradit', weight=118)
G.add_edge('Kamphaeng Phet', 'Tak', weight=68)
G.add_edge('Kamphaeng Phet', 'Phichit', weight=90)
G.add_edge('Kamphaeng Phet', 'Nakhonsawan', weight=117)
G.add_edge('Kamphaeng Phet', 'Sukhothai', weight=77)
G.add_edge('Kamphaeng Phet', 'Phitsanulok', weight=103)
G.add_edge('Phichit', 'Phitsanulok', weight=73)
G.add_edge('Phichit', 'Kamphaeng Phet', weight=90)
G.add_edge('Phichit', 'Nakhonsawan', weight=113)
G.add_edge('Phichit', 'Phetchabun', weight=129)
G.add_edge('Nakhonsawan', 'Phichit', weight=113)
G.add_edge('Nakhonsawan', 'Phetchabun', weight=184)
G.add_edge('Nakhonsawan', 'Kamphaeng Phet', weight=117)
G.add_edge('Nakhonsawan', 'Uthai Thani', weight=50)
G.add_edge('Nakhonsawan', 'Tak', weight=185)
G.add_edge('Phetchabun', 'Phichit', weight=129)
G.add_edge('Phetchabun', 'Phitsanulok', weight=170)
G.add_edge('Phetchabun', 'Nakhonsawan', weight=184)
G.add_edge('Uthai Thani', 'Tak', weight=234)
G.add_edge('Uthai Thani', 'Nakhonsawan', weight=50)
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