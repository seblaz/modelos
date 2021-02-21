import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from collections import Counter
import os

def count_days(days_software, days_heuristic):
    '''
    input:
    days_software, days_heuristic = graphs ej: [(color, vecino), (color, vecino), ..]


    days = todos los dias ( soft y heu)

    output:
    days_software = {day: cantidad de vecinos ..} para todos los days
    days_heuristic = {day: cantidad de vecinos ..} para todos los days
    '''
    list1 = list(map(lambda x: x[0], days_software))
    list2 = list(map(lambda x: x[0],days_heuristic))
    days = set(list1)
    days.update(list2)

    counter_software = {day:0 for day in days}
    counter_heuristic = counter_software.copy()

    for day, family in days_software: 
        counter_software[day] += 1
    for day, family in days_heuristic: 
        counter_heuristic[day] += 1
    return counter_software, counter_heuristic, days

def generate_family_per_day(days_software, days_heuristic, model):
    '''
    days_software, days_heuristic = List with tuple (day, family group)
    '''
    
    counter_software, counter_heuristic, days = count_days(days_software, days_heuristic)
    
    df = pd.DataFrame({'day': list(days), 'Modelo': list(counter_software.values()), 'Heuristica': list(counter_heuristic.values())})
    
    barWidth = 0.3
    # multiple line plot
    plt.figure()
    plt.plot('day', 'Modelo','o',data=df, color='#499030')
    plt.plot('day', 'Heuristica',   'x', data=df, color='#8313D1')

    plt.xlabel('Días')
    plt.ylabel('Cantidad de grupos familiares')
    plt.legend()
    plt.savefig(f'family_per_day_{model}.png')

def generate_days_per_trimester(days_software_1, days_software_2, days_heuristic_1, days_heuristic_2):

    trimester = 90

    list1 = list(map(lambda x: x[0],days_software_1))
    list2 = list(map(lambda x: x[0],days_software_2))
    n_days_software = list(map(lambda x: trimester/x, [len(Counter(list1)), len(Counter(list2))]))
    
    list1 = list(map(lambda x: x[0],days_heuristic_1))
    list2 = list(map(lambda x: x[0],days_heuristic_2))
    n_days_heuristic = list(map(lambda x: trimester/x, [len(Counter(list1)), len(Counter(list2))]))
    
    barWidth = 0.3
    r1 = np.arange(len(n_days_software))
    r2 = [x + barWidth for x in r1]
    
    # Create software bars
    plt.figure()
    plt.bar(r1, n_days_software, width = barWidth, color = '#DE7EC1', label='Resolución con software')
    
    # Create heuristic bars
    plt.bar(r2, n_days_heuristic, width = barWidth, color = '#1419B2', label='Resolución con Heurística')
    
    # general layout
    plt.xticks([(r + barWidth / 2) for r in range(len(n_days_software))], ['Dataset Entrega', 'Dataset Grande'])
    plt.ylabel('Cantidad de salidas de un grupo familiar por trimestre')
    plt.legend()
    
    # Show graphic
    plt.savefig('days_per_year.png')


def initilialize_solution(model, dataset):
    filename = os.path.join('output', 'sol-{}-{}.csv').format(model, dataset)

    with open(filename, 'r') as file:
        graph = []
        # [(diaX: vecinoX), (diaY:vecinoY), ..]
        file.readline()     # skip header
        for line in file: 
            line = line.rstrip().split(',')
            graph.append((int(line[1]), int(line[0])))
    return graph


def get_parity(graph):
    tot_population = len(graph)
    n_days = max(graph, key=lambda x: x[0])[0]
    day_frequencies = Counter(map(lambda x: x[0], graph))
    parity = 0
    print(day_frequencies)
    for day in day_frequencies:
        parity += abs(day_frequencies[day] - (tot_population / n_days))
    return parity


def generate_parities(software_entrega_graph, heuristic_entrega_graph, software_grande_graph, heuristic_grande_graph):

    barWidth = 0.33

    bar_modelo = list(map(get_parity, [software_entrega_graph, software_grande_graph]))
    bar_heuristica = list(map(get_parity, [heuristic_entrega_graph, heuristic_grande_graph]))

    r1 = np.arange(len(bar_modelo))
    r2 = [x + barWidth for x in r1]
    
    plt.figure()
    plt.bar(r1, bar_modelo, color='#7f6d5f', width=barWidth, edgecolor='white', label='Modelo')
    plt.bar(r2, bar_heuristica, color='#557f2d', width=barWidth, edgecolor='white', label='Heuristica')
    
    plt.xlabel('Set de datos', fontweight='bold')
    plt.xticks([(r + barWidth / 2) for r in range(len(bar_modelo))], ['Entrega', 'Grande'])
    plt.ylabel('Paridad entre cantidad de salidas por día')


    plt.legend()
    plt.savefig('parities.png')


def main():

    software_entrega_graph = initilialize_solution('modelo', 'entrega')
    heuristic_entrega_graph = initilialize_solution('heuristica', 'entrega')
    software_grande_graph = initilialize_solution('modelo', 'grande')
    heuristic_grande_graph = initilialize_solution('heuristica', 'grande')

    generate_parities(software_entrega_graph, heuristic_entrega_graph, software_grande_graph, heuristic_grande_graph)

    generate_family_per_day(software_entrega_graph, heuristic_entrega_graph, 'entrega')

    generate_family_per_day(software_grande_graph, heuristic_grande_graph, 'grande')

    generate_days_per_trimester(software_entrega_graph, software_grande_graph, heuristic_entrega_graph, heuristic_grande_graph)

    


if __name__ == '__main__':
    main()