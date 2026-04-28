from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from structures.graph import Graph
from structures.kd_tree import KDTree
from structures.hash_table import HashTable
from algorithms.dijkstra import dijkstra

app = Flask(__name__)
CORS(app)

def load_city_data():
    with open("data/sample_city.json", "r", encoding="utf-8") as file:
        return json.load(file)

city_data = load_city_data()

stop_table = HashTable()
for stop in city_data["stops"]:
    stop_table.put(stop["id"], stop)

graph = Graph()
for stop in city_data["stops"]:
    graph.add_vertex(stop["id"])

for connection in city_data["connections"]:
    graph.add_edge(
        connection["from"],
        connection["to"],
        connection["time"],
        {
            "distance": connection["distance"],
            "time": connection["time"],
            "line": connection["line"]
        }
    )

kd_tree = KDTree(city_data["stops"])

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Akilli Toplu Tasima ve Navigasyon Sistemi API calisiyor."
    })

@app.route("/api/stops", methods=["GET"])
def get_stops():
    return jsonify(city_data["stops"])

@app.route("/api/connections", methods=["GET"])
def get_connections():
    return jsonify(city_data["connections"])

@app.route("/api/nearest", methods=["POST"])
def nearest_stops():
    data = request.get_json()

    x = float(data.get("x"))
    y = float(data.get("y"))
    k = int(data.get("k", 3))

    nearest = kd_tree.k_nearest((x, y), k)
    return jsonify(nearest)

@app.route("/api/route", methods=["POST"])
def calculate_route():
    data = request.get_json()

    start = data.get("start")
    target = data.get("target")

    path, total_cost = dijkstra(graph, start, target)
    path_stops = [stop_table.get(stop_id) for stop_id in path]

    return jsonify({
        "path": path,
        "pathStops": path_stops,
        "totalCost": total_cost
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)