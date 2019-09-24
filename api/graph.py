from flask import Blueprint, send_file, request
import igraph as ig

blueprint = Blueprint('graph', __name__)

@blueprint.route('/graphs', methods=['POST'])
def upload_graph():
    filename = request.json['filename']
    ggraph = g.Graph.Read_GraphML('exercise/networks/NREN.graphml')
