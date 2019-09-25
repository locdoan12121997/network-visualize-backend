from flask import g
from flask import current_app

def get_graph_name(_graphname=None):
    with current_app.app_context():
        if not 'graphname' in g:
            g.graphname = _graphname
            print(g.graphname)
        # if _graphname:
        #     print(_graphname)
        #     g.graphname = _graphname
        return g.graphname
