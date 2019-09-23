from flask import Blueprint, send_file

blueprint = Blueprint('graph', __name__)
@blueprint.route('/edges', methods=['POST'])
def create_new_graph():
    return "ok"