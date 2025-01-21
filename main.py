from flask import Flask, request, jsonify, render_template
import json
from collections import deque

app = Flask(__name__)

# Load the adjacency list
def load_adjacency_list(file_path):
    try:
        with open(file_path, 'r') as f:
            adjacency_list = json.load(f)  # Ensure your file is JSON-formatted
        return adjacency_list
    except Exception as e:
        print(f"Error loading adjacency list: {e}")
        return {}
    
ADJACENCY_LIST_FILE = './adjacency_list.json'
adjacency_list = load_adjacency_list(ADJACENCY_LIST_FILE)

# Perform BFS search
def bfs_with_path(start, target):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path  # Return the path when target is found

        for neighbor in adjacency_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Return None if target is not found


@app.route('/')
def index():
    return render_template('index.html')
    # return("Hello")


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    start = data.get('start')
    target = data.get('target')

    # Perform BFS search
    path = bfs_with_path(start, target)

    if path:
        return jsonify({"path": " -> ".join(path)})
    else:
        return jsonify({"error": "No connection found."})
    
@app.route('/adjacency-list', methods=['GET'])
def get_adjacency_list():
    return jsonify(adjacency_list)  # Serve the adjacency list


if __name__ == '__main__':
    app.run(debug=True)
