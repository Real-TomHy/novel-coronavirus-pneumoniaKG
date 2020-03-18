from flask import Flask, jsonify, render_template
from py2neo import Graph, authenticate
app = Flask(__name__)
graph = Graph('http://neo4j:1210991856hy@localhost:7474/db/data/')
def buildNodes(nodeRecord):
    data = {"id": nodeRecord['n'].__name__, "label": str(nodeRecord['n']._Node__labels)}
    data.update(nodeRecord['n'])

    return {"data": data}

def buildEdges(relationRecord):
    data = {"source": str(relationRecord['r'].start_node().__name__),
                       "target": str(relationRecord['r'].end_node().__name__),
                       "relationship": relationRecord['r']._Relationship__type}

    return {"data": data}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def get_graph():
    nodes = list(map(buildNodes, graph.run('MATCH (n) RETURN n LIMIT 25')))
    edges = list(map(buildEdges, graph.run('MATCH ()-[r]->() RETURN r LIMIT 25')))

    return jsonify(elements = {"nodes": nodes, "edges": edges})

if __name__ == '__main__':
    app.run(debug = True)