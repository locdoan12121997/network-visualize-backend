from flask import Blueprint, send_file, request, Response
import igraph as ig

from util import get_graph_file

blueprint = Blueprint('graph', __name__)

@blueprint.route('/graphs', methods=['GET'])
def upload_graph():
    filename = request.json['filename']
    graph_name = get_graph_file(filename)
    return send_file(graph_name), 200


@blueprint.route('/graphs', methods=['POST'])
def save_graph():
    filename = request.json['filename']
    graph_name = get_graph_file()
    graph = ig.Graph.Read_GraphML(graph_name)
    graph.write_graphml('static/' + filename)
    return Response("Save succedded", 201)
