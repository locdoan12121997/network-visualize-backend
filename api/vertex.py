from flask import Blueprint, jsonify, request, make_response
from igraph import Graph, Vertex

blueprint = Blueprint('vertex', __name__)

graph_as_input = Graph.Read_GraphML("./api/mock/NREN.graphml")


@blueprint.route('/vertices', methods=['GET'])
def get_vertices():
    #   args = {
    #      "vertices": [ints or None]
    #   }

    args = request.json
    vertex_list = args["vertices"]

    vertex_dict = vertex_dictify(vertex_list)

    return jsonify(vertex_dict)


@blueprint.route('/vertices', methods=['POST'])
def add_vertices():
    #   args = {
    #      "vertices": int
    #   }

    args = request.json
    vertex_count = args["vertices"]

    graph_as_input.add_vertices(vertex_count)

    response = {"action": "Create", "code": "Success"}
    return make_response(jsonify(response), 201)


@blueprint.route('/vertices', methods=['PUT'])
def edit_vertex():  # for now, can only edit one vertex at a time
    #    args = {
    #       "vertex": int,
    #       "attribute_name": string,
    #       "new_value": string or int
    #    }

    args = request.json
    vertex_id = args["vertex"]
    attr = args["attribute_name"]
    new_value = args["new_value"]

    vertex = graph_as_input.vs[vertex_id]
    vertex[attr] = new_value

    response = {"action": "Edit", "code": "Success"}
    return make_response(jsonify(response), 201)


@blueprint.route('/vertices', methods=['DELETE'])
def delete_vertices():
    #    args = {
    #       "attribute_name": string,
    #       "value": string or int
    #    }

    args = request.json
    attr = args["attribute_name"]
    value = args["value"]

    if attr == "index" :
        vertex_list = value
        edge_list = [edge.index for edge in graph_as_input.es if edge.source == value or edge.target == value]
    else:
        vertex_list = [vertex.index for vertex in graph_as_input.vs if vertex[attr] == value]
        edge_list = [edge.index for edge in graph_as_input.es if edge.source in vertex_list or edge.target in vertex_list]

    graph_as_input.delete_vertices(vertex_list)
    graph_as_input.delete_edges(edge_list)

    return str(graph_as_input)


# Local Functions
def vertex_dictify(vertex_list):
    vertex_dict = {}
    attributes = graph_as_input.vs.attributes()

    if len(vertex_list) == 0:
        vertex_list = graph_as_input.vs

    for vertex_id in vertex_list:
        if isinstance(vertex_id, Vertex):
            vertex = vertex_id
        else:
            vertex = graph_as_input.vs[vertex_id]
        append_vertex_to_dictionary(vertex_dict, attributes, vertex)

    return vertex_dict


def append_vertex_to_dictionary(dictionary, attributes, vertex):
    index = str(vertex.index)

    dictionary[index] = {}

    for attr in attributes:
        dictionary[index][attr] = str(vertex[attr])
