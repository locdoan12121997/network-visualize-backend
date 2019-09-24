from flask import Blueprint, jsonify
from igraph import Graph, Edge, EdgeSeq

blueprint = Blueprint('edge', __name__)

graph_as_input = Graph.Read_GraphML("./api/mock/NREN.graphml")


@blueprint.route('/get_edges', methods=['GET'])
def get_edges(*args):
    if len(args) == 0:
        edge_dict = edge_dictify(graph_as_input.es)
    elif isinstance(args[0], int):
        edge = graph_as_input.es[args[0]]

        edge_dict = edge_dictify(edge)
    elif isinstance(args[0], list) and not isinstance(args[0][0], tuple):
        edge_list = []

        for edge_id in args[0]:
            edge_list.append(graph_as_input.es[edge_id])

        edge_dict = edge_dictify(edge_list)
    else:
        edge_list = []

        for (source, target) in args[0]:
            edge = graph_as_input.es[graph_as_input.get_eid(source, target)]
            edge_list.append(edge)

        edge_dict = edge_dictify(edge_list)

    return jsonify(edge_dict)


@blueprint.route('/add_edges', methods=['GET'])
def add_edges(*args):
    if len(args) == 0:
        raise ValueError("expected at least one argument")
    else:
        graph_as_input.add_edges(args[0])
        return "ok"


@blueprint.route('/delete_edges', methods=['GET'])
def delete_edges(edge_list=None):
    graph_as_input.delete_edges(edge_list)
    return "ok"


# Local Functions
def edge_dictify(*args):
    edge_dict = {}
    attributes = graph_as_input.es.attributes()
    edges = args[0]

    if isinstance(edges, (list, EdgeSeq)):
        for edge in edges:
            append_edge_to_dictionary(edge_dict, attributes, edge)
    elif isinstance(edges, Edge):
        append_edge_to_dictionary(edge_dict, attributes, edges)

    return edge_dict


def append_edge_to_dictionary(dictionary, attributes, edge):
    index = str(edge.index)

    dictionary[index] = {}
    dictionary[index]["source"] = str(edge.source)
    dictionary[index]["target"] = str(edge.target)

    for attr in attributes:
        dictionary[index][attr] = str(edge[attr])
