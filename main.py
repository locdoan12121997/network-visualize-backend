from flask import Flask
from api.edge import blueprint as edge_bp
from api.graph import blueprint as graph_bp
from api.mock.graph import blueprint as mock_graph_bp
import igraph

app = Flask(__name__)

app.register_blueprint(edge_bp)
app.register_blueprint(graph_bp)
app.register_blueprint(mock_graph_bp)
g = igraph.Graph()


@app.route('/')
def home():
    return "This is the homepage";


if __name__ == '__main__':
    app.run()
