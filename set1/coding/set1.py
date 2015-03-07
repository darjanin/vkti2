#!/usr/bin/env python3

def read_input():
    count = int(input())

    edges = []

    for u in range(count):
        row = input().split(' ')
        for v, c in enumerate(row):
            edges.append((u, v, int(c)))

    return {'count': count, 'edges': edges}

def kruskal(count, edges):
    result = []
    sets = []

    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    for i in range(count): sets.append({i})

    for (u,v,c) in sorted_edges:
        if len(result) == count - 1: break

        if sets[u].isdisjoint(sets[v]):
            result.append((u, v, c))
            sets[v] = sets[u] = sets[u].union(sets[v])

    return result

def kruskal_price(edges):
    total = 0
    for (u,v,c) in edges:
        total += c
    return total

def tsp(edges):
    result = []

    for (u, v, c) in edges:
        if (u not in result): result.append(u)
        if (v not in result): result.append(v)

    result.append(result[0])

    return result

def tsp_price(vertices, edges, count):
    total = 0
    for idx in range(len(vertices)-1):
        total += edges[vertices[idx]*count + vertices[idx+1]][2]
    total += edges[vertices[0]*count + vertices[-1]][2]

    return total

if __name__ == '__main__':
    data = read_input()

    kruskal_result = kruskal(data['count'], data['edges'])
    print(kruskal_result)
    kruskal_price_value = kruskal_price(kruskal_result)
    print(kruskal_price_value)

    tsp_result = tsp(kruskal_result)
    print(tsp_result)
    tsp_price_value = tsp_price(tsp_result, data['edges'], data['count'])
    print(tsp_price_value)
