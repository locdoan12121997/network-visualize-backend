from flask import Blueprint, send_file, request, g
import igraph as ig

from util import get_graph

blueprint = Blueprint('graph', __name__)

@blueprint.route('/graphs', methods=['POST'])
def upload_graph():
    filename = request.json['filename']
    graph = get_graph(filename)
    return send_file(filename), 201
