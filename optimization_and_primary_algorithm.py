import line_profiler
import sys
import networkx as nx
import numpy as np
global path_nodes
# Initialize Graph
G = nx.Graph()
# Define nodes number
n = 128
# Watts-Strogtaz Initialization
G = nx.watts_strogatz_graph(n, 4, 0, seed=None)
# Erdos-Renyi Initialization
# G = nx.erdos_renyi_graph(n, 2*(np.log(n))/n)

# Randomly assign weight on edges
for u, v, w in G.edges(data=True):
    w['omit'] = 0
    w['weight'] = np.random.randint(1, 10)

graph = nx.get_edge_attributes(G, 'weight')
# Initialize dict for path determination
endpoint = {}
endpoint1 = {}
path_list = {}
redundant = {}
path_dict = {}


# Optimized Algorithm
def flag():
    sorted_graph = dict(sorted(graph.items(), key=lambda item: item[1],
                        reverse=True))
    for (key, value) in sorted_graph.items():
        if redundant.get(key[0]):
            continue
        elif redundant.get(key[1]):
            continue
        elif path_dict.get(key[0]) is None and path_dict.get(key[1]) is None:
            path_list[key[0], key[1]] = value
            path_dict[key[0]] = 0
            path_dict[key[1]] = 0
            endpoint[key[0]] = key[1]
            endpoint1[key[1]] = key[0]
        elif path_dict.get(key[0]) is None:
            if endpoint.get(key[1]):
                redundant[key[1]] = 1
                path_list[key[0], key[1]] = value
                path_dict[key[0]] = 0
                k = endpoint[key[1]]
                endpoint[key[0]] = k
                del endpoint[key[1]]
                endpoint1.update({k: key[0]})
            elif endpoint1.get(key[1]):
                redundant[key[1]] = 1
                path_list[key[0], key[1]] = value
                path_dict[key[0]] = 0
                a = endpoint1[key[1]]
                endpoint.update({a: key[0]})
                del endpoint1[key[1]]
                endpoint1[key[0]] = a
        elif path_dict.get(key[1]) is None:
            if endpoint.get(key[0]):
                redundant[key[0]] = 1
                path_list[key[0], key[1]] = value
                path_dict[key[1]] = 0
                k = endpoint[key[0]]
                endpoint1.update({k: key[1]})
                endpoint[key[1]] = k
                del endpoint[key[0]]
            elif endpoint1.get(key[0]):
                redundant[key[0]] = 1
                path_list[key[0], key[1]] = value
                path_dict[key[1]] = 0
                a = endpoint1[key[0]]
                endpoint.update({a: key[1]})
                del endpoint1[key[0]]
                endpoint1[key[1]] = a
        elif endpoint.get(key[1]):
            if endpoint.get(key[0]):
                redundant[key[1]] = 1
                redundant[key[0]] = 1
                path_list[key[0], key[1]] = value
                v1 = endpoint[key[1]]
                v0 = endpoint[key[0]]
                endpoint[v1] = v0
                del endpoint1[v0]
                del endpoint1[v1]
                endpoint1[v0] = v1
                del endpoint[key[1]]
                del endpoint[key[0]]

            elif endpoint1.get(key[0]):
                if endpoint[key[1]] != key[0]:
                    redundant[key[1]] = 1
                    redundant[key[0]] = 1
                    path_list[key[0], key[1]] = value
                    end_1 = endpoint[key[1]]
                    end_0 = endpoint1[key[0]]
                    del endpoint1[key[0]]
                    endpoint1.update({end_1: end_0})
                    del endpoint[key[1]]
                    endpoint.update({end_0: end_1})

        elif endpoint1.get(key[1]):

            if endpoint1.get(key[0]):
                redundant[key[1]] = 1
                redundant[key[0]] = 1
                path_list[key[0], key[1]] = value
                end_1 = endpoint1[key[1]]
                end_0 = endpoint1[key[0]]
                del endpoint[end_1]
                endpoint.update({end_0: end_1})
                del endpoint1[key[1]]
                del endpoint1[key[0]]
                endpoint1[end_1] = end_0

            elif endpoint.get(key[0]):
                if endpoint[key[0]] != key[1]:
                    redundant[key[1]] = 1
                    redundant[key[0]] = 1
                    path_list[key[0], key[1]] = value
                    end_1 = endpoint1[key[1]]
                    end_0 = endpoint[key[0]]
                    del endpoint[key[0]]
                    del endpoint[end_1]
                    endpoint[end_1] = end_0
                    del endpoint1[key[1]]
                    del endpoint1[end_0]
                    endpoint1[end_0] = end_1


# Primary Algorithm
def no_flag():
    sorted_graph = dict(sorted(graph.items(), key=lambda item: item[1],
                    reverse=True))
    for (key, value) in sorted_graph.items():
        if path_dict.get(key[0]) is None and path_dict.get(key[1]) is None:
            path_list[key[0], key[1]] = value
            path_dict[key[0]] = 0
            path_dict[key[1]] = 0
            endpoint[key[0]] = key[1]
            endpoint1[key[1]] = key[0]
        elif path_dict.get(key[0]) is None:
            if endpoint.get(key[1]):
                path_list[key[0], key[1]] = value
                path_dict[key[0]] = 0
                k = endpoint[key[1]]
                endpoint[key[0]] = k
                del endpoint[key[1]]
                endpoint1.update({k: key[0]})
            elif endpoint1.get(key[1]):
                path_list[key[0], key[1]] = value
                path_dict[key[0]] = 0
                a = endpoint1[key[1]]
                endpoint.update({a: key[0]})
                del endpoint1[key[1]]
                endpoint1[key[0]] = a
        elif path_dict.get(key[1]) is None:
            if endpoint.get(key[0]):
                path_list[key[0], key[1]] = value
                path_dict[key[1]] = 0
                k = endpoint[key[0]]
                endpoint1.update({k: key[1]})
                endpoint[key[1]] = k
                del endpoint[key[0]]
            elif endpoint1.get(key[0]):
                path_list[key[0], key[1]] = value
                path_dict[key[1]] = 0
                a = endpoint1[key[0]]
                endpoint.update({a: key[1]})
                del endpoint1[key[0]]
                endpoint1[key[1]] = a
        elif endpoint.get(key[1]):
            if endpoint.get(key[0]):
                path_list[key[0], key[1]] = value
                v1 = endpoint[key[1]]
                v0 = endpoint[key[0]]
                endpoint[v1] = v0
                del endpoint1[v0]
                del endpoint1[v1]
                endpoint1[v0] = v1
                del endpoint[key[1]]
                del endpoint[key[0]]
            elif endpoint1.get(key[0]):
                if endpoint[key[1]] != key[0]:
                    path_list[key[0], key[1]] = value
                    end_1 = endpoint[key[1]]
                    end_0 = endpoint1[key[0]]
                    del endpoint1[key[0]]
                    endpoint1.update({end_1: end_0})
                    del endpoint[key[1]]
                    endpoint.update({end_0: end_1})
        elif endpoint1.get(key[1]):
            if endpoint1.get(key[0]):
                path_list[key[0], key[1]] = value
                end_1 = endpoint1[key[1]]
                end_0 = endpoint1[key[0]]
                del endpoint[end_1]
                endpoint.update({end_0: end_1})
                del endpoint1[key[1]]
                del endpoint1[key[0]]
                endpoint1[end_1] = end_0
            elif endpoint.get(key[0]):
                if endpoint[key[0]] != key[1]:
                    path_list[key[0], key[1]] = value
                    end_1 = endpoint1[key[1]]
                    end_0 = endpoint[key[0]]
                    del endpoint[key[0]]
                    del endpoint[end_1]
                    endpoint[end_1] = end_0
                    del endpoint1[key[1]]
                    del endpoint1[end_0]
                    endpoint1[end_0] = end_1


prof = line_profiler.LineProfiler(flag)
prof.enable()
flag()
prof.disable()
prof.print_stats(sys.stdout)

endpoint = {}
endpoint1 = {}
path_list = {}
redundant = {}
path_dict = {}

prof = line_profiler.LineProfiler(no_flag)
prof.enable()  # 开始性能分析
no_flag()
prof.disable()  # 停止性能分析
prof.print_stats(sys.stdout)
