from flask import Blueprint

blueprint = Blueprint('edge', __name__)

@blueprint.route('/edges')
def get_all_edges():
    return "ok"