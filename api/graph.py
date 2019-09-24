from flask import Blueprint, send_file, request, g
import igraph as ig

blueprint = Blueprint('graph', __name__)

@blueprint.route('/graphs', methods=['POST'])
def upload_graph():
    filename = request.json['filename']
    graph = ig.Graph.Read_GraphML(filename)

