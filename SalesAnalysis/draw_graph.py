import networkx as nx
import matplotlib.pyplot as plt


def create_corr_network(G, corr_tresh=0.1):

    # Create copy of G
    H = G.copy()

    # Remove edges based on condition
    for node1, node2, metadata in H.edges(data=True):
        if metadata['weight'] < corr_tresh:
            G.remove_edge(node1, node2)

    # Create a list of edges and weights
    edges, _ = zip(*nx.get_edge_attributes(G, 'weight').items())

    # Positions in the vizualization
    positions = nx.circular_layout(G)

    # Figure configuration
    plt.figure(figsize=(8, 8))

    # Draw nodes
    nx.draw_networkx_nodes(
        G, positions, node_color='#0099ff', node_size=500, alpha=0.8)

    # Styling for labels
    nx.draw_networkx_labels(
        G, positions, font_size=8, font_family='sans-serif')

    # Draws the edges
    nx.draw_networkx_edges(G, positions, edge_list=edges, style='solid')

    # Displays the graph without axis
    plt.axis('off')

    # Saves image
    plt.savefig("graph1.png", format="PNG", dpi=320)

    # Show Image
    plt.show()

    return
