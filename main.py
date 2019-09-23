from flask import Flask
from api.edge import blueprint as edge_bp
import igraph

app = Flask(__name__)
app.register_blueprint(edge_bp)
g = igraph.Graph()

if __name__ == '__main__':
    app.run()
