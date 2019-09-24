from flask import Blueprint, send_file
from igraph import *

blueprint = Blueprint('mock_graph', __name__)


@blueprint.route('/mock_graph', methods=['POST'])
def get_graph():
    try:
        return send_file("./api/mock/NREN.graphml")
    except Exception as e:
        return str(e)
