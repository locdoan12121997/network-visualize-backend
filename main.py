from flask import Flask

from api.edge import blueprint as edge_bp
from api.graph import blueprint as graph_bp

app = Flask(__name__)
app.register_blueprint(edge_bp)
app.register_blueprint(graph_bp)


if __name__ == '__main__':
    app.run()
