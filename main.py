import matplotlib.pyplot as plt
import time
import networkx as nx
import os, sys
from networkx import Graph

from heuristica import HeuristicaGreedy
from parser import Parser

def create_graph(nodes, edges):
    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def write_output(graph, filename):
    with open(filename, 'w') as f:
        f.write('vecino,dia\n')
        arr = list(graph.nodes(data=True))
        arr.sort(key=lambda x: x[1]["dia"])
        for node in arr:
            f.write(f'{node[0]},{str(node[1]["dia"])}\n')


def create_folder(path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.mkdir(dirname)


def main():
    if len(sys.argv) < 2:
        print('Fata parametro de dataset [prueba/entrega/grande/enorme]\n')
        print('Uso:\tpython main.py <dataset>\n')
        return

    FILE_PATH = os.path.join('datasets', 'dataset_{}.txt').format(sys.argv[1])
    OUTPUT_PATH = os.path.join('output', 'sol-heuristica-{}.csv').format(sys.argv[1])

    create_folder(FILE_PATH)
    create_folder(OUTPUT_PATH)

    parser = Parser(FILE_PATH)
    graph = create_graph(parser.nodes, parser.edges)
    start = time.time()
    graph = HeuristicaGreedy().calculate(graph)
    print(f"Tiempo de ejecución: {time.time() - start} seg")

    if graph:
        node_map = []
        for node in graph.nodes(data=True):
            node_map.append(node[1]['dia'])

        write_output(graph, OUTPUT_PATH)

        # nx.draw(graph, node_color=node_map)
        # plt.show()



if __name__ == '__main__':
    main()