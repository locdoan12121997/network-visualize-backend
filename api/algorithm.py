from flask import Blueprint, request, jsonify
from igraph import Graph, InternalError
from api.edge import edge_dictify

blueprint = Blueprint('algorithm', __name__)

graph_as_input = Graph.Read_GraphML("./api/mock/NREN.graphml")


# graph_as_input = Graph.Erdos_Renyi(n=1000000, m=3000000)
# generate random graph n = #vertices, p = edge prob, m = #edges


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


@blueprint.route('/algorithms/bottleneck', methods=['GET'])
def b():
    #   args = {
    #       "source": <source vertex index>,
    #       "target": <target vertex index>,
    #       "output": "EDGE" return list of edges, "VERTEX" return list of vertex lists of nodes on each partition
    #   }

    args = request.json
    source = args["source"]
    target = args["target"]
    output = args["output"]

    cut = graph_as_input.maxflow(source, target, "LinkSpeedRaw")

    if output == "EDGE":
        bottleneck_edge = []
        for vt_a_id in cut[0]:
            for vt_b_id in cut[1]:
                vt_a = graph_as_input.vs[vt_a_id]
                vt_b = graph_as_input.vs[vt_b_id]
                try:
                    edge_id = graph_as_input.get_eid(vt_a.index, vt_b.index)
                except InternalError:
                    continue
                bottleneck_edge.append(graph_as_input.es[edge_id])

        return jsonify(edge_dictify(bottleneck_edge))
    elif output == "VERTEX":
        partition_list = [cut[0], cut[1]]

        return jsonify(partition_list)
