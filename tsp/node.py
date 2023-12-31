class Node:
    def __init__(self, number, nodes_list):
        self.__number = number
        self.__distances = self.__init_distances(nodes_list)

    def get_distance(self, node):
        return self.__distances[node.get_number()]
    
    def get_number(self):
        return self.__number

    def __init_distances(self, nodes_list):
        return { (node[0] if node[1] == self.__number else node[1]) : node[2] for node in nodes_list }
        