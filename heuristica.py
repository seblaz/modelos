COLORS = [
    'yellow',
    'red',
    'green',
    'blue',
    'orange',
    'purple',
    'white',
    'pink',
    'a',
    'b',
    'c'
]


def split(x, n):
    # If we cannot split the
    # number into exactly 'N' parts
    if x < n:
        return False

        # If x % n == 0 then the minimum
    # difference is 0 and all
    # numbers are x / n
    elif x % n == 0:
        return [x // n for _ in range(n)]

    # upto n-(x % n) the values
    # will be x / n
    # after that the values
    # will be x / n + 1
    zp = n - (x % n)
    pp = x // n
    result = []
    for i in range(n):
        if i >= zp:
            result.append(pp + 1)
        else:
            result.append(pp)
    result.reverse()
    return result



class HeuristicaGreedy:
    """
    1. colores = []
    2. Mientras(no se encuentre solución):
    3.   reiniciar_grafo()
    4.   colores.agregar(un_color)
    5.   vértices_por_color = split(cantidad(grafo.vertices), cantidad(colores))

    6.   for index, cantidad in vértices_por_color:
    7.     color = colores[index]
    8.     colorear "cantidad" de vértices con "color"
    """

    def calculate(self, graph_i):
        # for i in range(5, len(COLORS)):
        for i in range(1, len(COLORS)):
            graph = graph_i.copy()
            if self._buscar_solucion(graph, i + 1):
                return graph
        return False

    def _buscar_solucion(self, graph, cantidad_de_colores):
        colores = COLORS[:cantidad_de_colores]
        vertices_por_color = split(len(graph.nodes), len(colores))

        for indice, cantidad in enumerate(vertices_por_color):
            color = colores[indice]

            for _ in range(cantidad):
                pude_colorear = False
                for nodo in graph.nodes(data=True):
                    ## TODO: verificar que el color no este en los vecinos
                    if self._vecino_de_nodo_tiene_color(graph, nodo, color):
                        continue

                    if 'color' not in graph.nodes[nodo[0]]:
                        graph.nodes[nodo[0]]['color'] = color
                        pude_colorear = True
                        break

                if not pude_colorear:
                    print('No encontré solución con {} colores'.format(len(colores)))
                    return False
        print('Encontré solución con {} colores'.format(len(colores)))
        return True


    def _vecino_de_nodo_tiene_color(self, graph, nodo, color):
        for vecino in graph.neighbors(nodo[0]):
            if ('color' in graph.nodes[vecino]) and (graph.nodes[vecino]['color']) == color:
                return True
        return False