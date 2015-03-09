#!/usr/bin/env python3
import random

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

def update_prices(edges, vertices):
    result_edges = []

    for (u, v, c) in edges:
        if (u != v):
            result_edges.append((u, v, c + vertices[u] + vertices[v]))
        else:
            result_edges.append((u, v, c))

    return result_edges

def kruskal_price(edges):
    total = 0
    for (u,v,c) in edges:
        total += c
    return total

def calculate_vertices(edges):
    vertex_count = {}
    for (u,v,c) in edges:
        if u in vertex_count:
            vertex_count[u] += 1
        else:
            vertex_count[u] = 1
        if v in vertex_count:
            vertex_count[v] += 1
        else:
            vertex_count[v] = 1

    vertex_count = sorted(vertex_count.items(), key=lambda item: item[1])

    vertices = []
    for idx in range(len(vertex_count)):
        vertices.append(0)
    total = 0
    counter = 0
    last = 0
    for (key, value) in vertex_count:
        if (value == 1):
            vertices[key] = -1
            total += -1
        else:
            vertices[key] = value - 1
            total += value - 1
    if total != 0:
        vertices[len(vertices)-1] += total
    return vertices

if __name__ == '__main__':
    data = read_input()

    kruskal_result = kruskal(data['count'], data['edges'])
    kruskal_price_value = kruskal_price(kruskal_result)

    vertices = calculate_vertices(kruskal_result)

    update_edges = update_prices(data['edges'], vertices)

    kruskal_result = kruskal(data['count'], update_edges)
    kruskal_price_value = kruskal_price(kruskal_result)

    result_str = []
    for item in vertices:
        result_str.append(str(item))
    print(" ".join(result_str))