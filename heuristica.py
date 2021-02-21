DIAS = [x for x in range(1, 1001)]


def split(x, n):
    '''
    Genera una lista de `n` enteros cuya suma da exactamente `x`.
    La diferencia entre los `n` enteros no será mayor a uno.
    '''
    if x < n:
        return False

    elif x % n == 0:
        return [x // n for _ in range(n)]

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

    def calculate(self, graph_i):
        for i in range(1, len(DIAS)):
            graph = graph_i.copy()
            if self._buscar_solucion(graph, i + 1):
                return graph
        return False

    def _buscar_solucion(self, graph, cantidad_de_dias):
        dias = DIAS[:cantidad_de_dias]
        grupos_por_dia = split(len(graph.nodes), len(dias))

        for indice, cantidad in enumerate(grupos_por_dia):
            dia = dias[indice]

            for _ in range(cantidad):
                pude_asignar_dia = False
                for nodo in graph.nodes(data=True):
                    if self._dia_asignable(graph, nodo, dia):
                        graph.nodes[nodo[0]]['dia'] = dia
                        pude_asignar_dia = True
                        break

                if not pude_asignar_dia:
                    print('No encontré solución con {} dias'.format(len(dias)))
                    return False

        print('Encontré solución con {} dias'.format(len(dias)))
        return True

    def _dia_asignable(self, graph, nodo, dia):
        return ('dia' not in graph.nodes[nodo[0]]) and (not self._vecino_de_nodo_tiene_mismo_dia(graph, nodo, dia))

    def _vecino_de_nodo_tiene_mismo_dia(self, graph, nodo, dia):
        for vecino in graph.neighbors(nodo[0]):
            if ('dia' in graph.nodes[vecino]) and (graph.nodes[vecino]['dia']) == dia:
                return True
        return False
