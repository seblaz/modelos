import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

from heuristica import HeuristicaGreedy
from parser import Parser

FILE_PATH = 'datasets/dataset_entrega.txt'


def create_graph(nodes, edges):
    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


if __name__ == '__main__':
    parser = Parser(FILE_PATH)
    graph = create_graph(parser.nodes, parser.edges)
    graph = HeuristicaGreedy().calculate(graph)

    if graph:
        node_map = []
        for node in graph.nodes(data=True):
            node_map.append(node[1]['color'])

        nx.draw(graph, node_color=node_map)
        # print(graph.nodes(data=True))
        plt.show()
