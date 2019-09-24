from flask import g
import igraph as ig

def get_graph(filename=None):
    if 'graph' not in g:
        g.graph = ig.Graph.Read_GraphML(filename)

    return g.graph
