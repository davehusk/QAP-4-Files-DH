'''
Dave Husk
dave.husk@keyin.com
Nov 24, 2023

This was my first attempt to visualize an ERD in 3d
'''

import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_3d_erd():
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a graph
    G = nx.Graph()

    # Add entities as nodes with some arbitrary positions
    entities = {
        'Customer': (0, 0, 0),
        'Room': (1, 1, 1),
        'RoomStatus': (2, 2, 2),
        'Bookings': (3, 3, 3),
        'Revenue': (4, 4, 4),
        'Supplies': (5, 5, 5),
        'Defaults': (6, 6, 6)
    }

    for entity, pos in entities.items():
        G.add_node(entity, pos=pos)

    # Define relationships (edges)
    relationships = [
        ('Customer', 'RoomStatus'), 
        ('Customer', 'Bookings'), 
        ('Customer', 'Revenue'), 
        ('Room', 'RoomStatus'), 
        ('Supplies', 'Room')  # Implied relationship
    ]

    G.add_edges_from(relationships)

    # Get positions
    pos = nx.get_node_attributes(G, 'pos')

    # Draw nodes
    for node, (x, y, z) in pos.items():
        ax.scatter(x, y, z, c='b', marker='o')
        ax.text(x, y, z, node)

    # Draw edges
    for edge in G.edges():
        x = np.array((pos[edge[0]][0], pos[edge[1]][0]))
        y = np.array((pos[edge[0]][1], pos[edge[1]][1]))
        z = np.array((pos[edge[0]][2], pos[edge[1]][2]))
        ax.plot(x, y, z, c='r')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.title("3D Entity-Relationship Diagram")

    plt.show()

create_3d_erd()
