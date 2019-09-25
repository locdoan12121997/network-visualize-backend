from flask import Blueprint, send_file, request, Response
import igraph as ig

from util import get_graph

blueprint = Blueprint('graph', __name__)

@blueprint.route('/graphs', methods=['GET'])
def upload_graph():
    filename = request.json['filename']
    graph = get_graph(filename)
    return send_file(filename), 200


@blueprint.route('/graphs', methods=['POST'])
def save_graph():
    filename = request.json['filename']
    graph = get_graph()
    # ig.Graph.write_graphml('static/' + filename)
    return Response("Save succedded", 201)
