import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
g.add_node(1)
g.add_node(4)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(3,4)
print g.degree()
print nx.degree_histogram(g)
pr = nx.pagerank(g, alpha = 0.85)
print pr
path = nx.all_pairs_shortest_path(g)
print path[1][4]
print nx.clustering(g)
nx.draw(g, node_size = 100, node_color = 'b', with_labels = False)
plt.show()