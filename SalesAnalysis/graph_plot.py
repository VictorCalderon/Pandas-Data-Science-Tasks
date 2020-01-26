import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def plot_corr_network(G, corr_tresh=-1, save_as=None, size_data='weight', scaling=500):
    """ Plot a correlation CircusPlot Graph """

    # Create copy of G
    H = G.copy()

    # Remove edges based on condition
    for node1, node2, metadata in G.edges(data=True):
        if metadata['weight'] < corr_tresh:
            H.remove_edge(node1, node2)

    # Create a list of edges and weights
    edges, weights = zip(*nx.get_edge_attributes(H, 'weight').items())

    if size_data == 'degree':
        # Degrees of each node as size in Graph
        degrees = dict(nx.degree(H))
        node_list, node_sizes = zip(*degrees.items())
        node_size = tuple([(scaling * (1 + x)**2) for x in node_sizes])

    else:
        # Create a list of nodes and size_data
        node_list, sizes = zip(*nx.get_node_attributes(H, size_data).items())
        node_size = tuple([scaling * x for x in sizes])

    # Scale weights to make them more visible
    weights = tuple([(1 + np.abs(x))**3 for x in weights])

    # Positions in the vizualization
    positions = nx.circular_layout(H)

    # Figure configuration
    plt.figure(figsize=(8, 8))

    # Draw nodes
    nx.draw_networkx_nodes(
        H, positions, node_color='#0099ff', nodelist=node_list,
        node_size=node_size, alpha=0.8)

    # Styling for labels
    nx.draw_networkx_labels(
        H, positions, font_size=8, font_family='sans-serif')

    # Draws the edges []
    nx.draw_networkx_edges(
        H, positions, edge_list=edges, style='solid', width=weights,
        edge_vmin=min(weights), edge_vmax=max(weights),
        edge_color=weights, edge_cmap=plt.cm.Blues
    )

    # Displays the graph without axis
    plt.axis('off')

    # Style
    plt.tight_layout()

    # Saves image
    if save_as:
        plt.savefig(f'{save_as}.png', dpi=320)

    # Show Image
    plt.show()
