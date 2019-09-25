from flask import Blueprint, jsonify, request, make_response
from igraph import Graph, Edge

blueprint = Blueprint('edge', __name__)

graph_as_input = Graph.Read_GraphML("./api/mock/NREN.graphml")


@blueprint.route('/edges', methods=['GET'])
def get_edges():
    #   args = {
    #       "edges": [{
    #           "source": int,
    #           "target": int
    #        },...]
    #   }
    #
    #    or
    #
    #    args = {
    #       "edges": [ints or None]
    #    }

    args = request.json
    edge_list = get_list(args)

    if len(edge_list) == 0:
        edge_dict = edge_dictify(graph_as_input.es)
    else:
        edge_dict = edge_dictify(edge_list)

    return jsonify(edge_dict)


@blueprint.route('/edges', methods=['POST'])
def add_edges():
    #   args = {
    #       "edges": [{
    #           "source": int,
    #           "target": int
    #        },...]
    #    }

    args = request.json
    edge_list = get_list(args)
    graph_as_input.add_edges(edge_list)

    response = {"action": "Create", "code": "Success"}
    return make_response(jsonify(response), 201)


@blueprint.route('/edges', methods=['PUT'])
def edit_edge():  # for now, can only edit one edge at a time
    # args = {
    #       "edge": {
    #           "source": int,
    #           "target": int
    #        },
    #       "attribute_name": string
    #       "new_value": string or int
    #   }
    #
    #    or
    #
    #    args = {
    #       "edge": int,
    #       "attribute_name": string
    #       "new_value": string or int
    #    }

    args = request.json
    edge_id = args["edge"]
    attr = args["attribute_name"]
    new_value = args["new_value"]

    if isinstance(edge_id, int):
        edge = graph_as_input.es[edge_id]
    else:
        edge = graph_as_input.es[graph_as_input.get_eid(edge_id["source"], edge_id["target"])]

    edge[attr] = new_value

    response = {"action": "Edit", "code": "Success"}
    return make_response(jsonify(response), 201)


@blueprint.route('/edges', methods=['DELETE'])
def delete_edges():
    #   args = {
    #       "edges": [{
    #           "source": int,
    #           "target": int
    #        },...]
    #   }
    #
    #    or
    #
    #    args = {
    #       "edges": [ints or None]
    #    }

    args = request.json
    edge_list = get_list(args)
    graph_as_input.delete_edges(edge_list)

    response = {"action": "Delete", "code": "Success"}
    return make_response(jsonify(response), 200)


# Local Functions
def edge_dictify(edge_list):
    edge_dict = {}
    attributes = graph_as_input.es.attributes()

    if len(edge_list) == 0:
        edge_list = graph_as_input.es

    for edge_id in edge_list:
        if isinstance(edge_id, Edge):
            edge = edge_id
        elif isinstance(edge_id, int):
            edge = graph_as_input.es[edge_id]
        else:
            edge = graph_as_input.es[graph_as_input.get_eid(edge_id[0], edge_id[1])]
        append_edge_to_dictionary(edge_dict, attributes, edge)

    return edge_dict


def append_edge_to_dictionary(dictionary, attributes, edge):
    index = str(edge.index)

    dictionary[index] = {}
    dictionary[index]["source"] = str(edge.source)
    dictionary[index]["target"] = str(edge.target)

    for attr in attributes:
        dictionary[index][attr] = str(edge[attr])


def get_list(json_obj):
    edges = json_obj["edges"]

    if len(edges) == 0:
        return []

    edge_list = []
    if isinstance(edges[0], int):
        for edge in edges:
            edge_list.append(edge)
    else:
        for st_tuple in edges:
            st = (st_tuple["source"], st_tuple["target"])
            edge_list.append(st)

    return edge_list
