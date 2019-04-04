import sys

# @ Name : Lane Gramling
# @ Due Date : April 4, 2019
# @ Brief: Topological Ordering
#  		Usage: python top_order_2766765.py input.txt > output.txt

edges = []      # Contains all edges, size |E|
graph = {}      # Contains the graph structure, constructed from edges

# Read in an adjacency list from a text file
def readAdjacencyList(filename):
    for line in open(filename, 'r').read().split('\n'):                                  # Read in file
        if line: edges.append(tuple(list(map(int, re.sub(r'\s', '', line).split(','))))) # Collect edges
    for u in list(set([u for (u, v) in edges])): graph[u] = []                  # Create all nodes 1..n
    for (u, v) in edges: graph[u].append(v)                                     # Add all edges to all nodes

# Compute a topological ordering, given a
def top_order():
    pass
















# Execution on runtime
if len(sys.argv) < 2:
    print("[Usage]: python top_order_2766765.py <input-file> > <output-file>")
else:
    readAdjacencyList(sys.argv[1])
    top_order()
