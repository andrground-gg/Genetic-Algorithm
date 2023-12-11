from utils import read_nodes_from_file, generate_nodes

if __name__ == "__main__":
    nodes_from_file = read_nodes_from_file('example.txt')
    nodes = generate_nodes(nodes_from_file)
