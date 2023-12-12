import numpy as np
from tsp.node import Node

def read_nodes_from_file(file_path):
    nodes = []
    with open(file_path) as f:
        nodes = np.array([line.rstrip().split(' ') for line in f]).astype(np.int32)

    return nodes

def generate_nodes(nodes_list):
    nodes = []
    uniques = np.unique(np.append(nodes_list[:, 0], nodes_list[:, 1]))

    for node_number in uniques:
        new_node = Node(node_number, nodes_list[(nodes_list[:, 0] == node_number) | (nodes_list[:, 1] == node_number)])
        nodes.append(new_node)

    return nodes

def get_total_cost(path_nodes):
    total_cost = 0
    for i in range(-1, len(path_nodes) - 1):
        total_cost += path_nodes[i].get_distance(path_nodes[i + 1])

    return total_cost