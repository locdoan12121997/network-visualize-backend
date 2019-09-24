from flask import Flask
from api.edge import blueprint as edge_bp
import igraph as ig

app = Flask(__name__)
app.register_blueprint(edge_bp)


def get_db(filename=None):
    if 'graph' not in g:
        g.graph = ig.Graph.Read_GraphML(filename)

    return g.graph

if __name__ == '__main__':
    app.run()
