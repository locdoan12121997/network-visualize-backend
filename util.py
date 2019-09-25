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


def get_graph_file(graphname=None):

    if graphname:
        f = open('static/graphname.txt', 'r+')
        current_name = f.read().strip('\n')
        f.seek(0)
        f.write(graphname)
        f.close()
        return graphname
    else:
        f = open('static/graphname.txt', 'r')
        current_name = f.read().strip('\n')
        f.close()
        return current_name
