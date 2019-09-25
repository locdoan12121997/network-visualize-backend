from flask import Blueprint, request, jsonify
from igraph import Graph

blueprint = Blueprint('algorithm', __name__)

graph_as_input = Graph.Read_GraphML("./api/mock/NREN.graphml")


@blueprint.route('/algorithms', methods=['GET'])
def get_shortest_paths():
    #   args = {
    #       "source": source node index,
    #       "target": [target node index/indices],
    #       "weights": <attribute name (as string) used as weight, if None, edges have equal weights>,
    #       "mode": <"OUT" calculate outgoing paths, "IN" calculate incoming paths, "ALL" calculate both>,
    #       "output": <"vpath" return list of vertices, "epath" return list of edges>
    #   }

    args = request.json
    source = args["source"]
    target = args["target"]
    weights = args["weights"]
    mode = args["mode"]
    output = args["output"]

    if len(target) == 0:
        target = None
    if weights == "":
        weights = None
    if mode == "":
        mode = "OUT"
    if output == "":
        output = "vpath"

    return jsonify(graph_as_input.get_shortest_paths(source, target, weights, mode, output))
