from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

size = 4
agent_pos = (0, 0)
pits = set()
wumpus = (0, 0)
visited = []
safe_cells = set()
path = []
inference_steps = 0

DIRS = [(0,1),(1,0),(-1,0),(0,-1)]

def in_bounds(x, y):
    return 0 <= x < size and 0 <= y < size

def generate_world(n):
    global pits, wumpus, agent_pos, visited, safe_cells, path

    pits.clear()
    visited.clear()
    safe_cells.clear()
    path.clear()
    agent_pos = (0,0)

    for _ in range(n):
        x, y = random.randint(0,n-1), random.randint(0,n-1)
        if (x,y) != agent_pos:
            pits.add((x,y))

    while True:
        w = (random.randint(0,n-1), random.randint(0,n-1))
        if w not in pits and w != agent_pos:
            return w

def get_percepts(x, y):
    breeze, stench = False, False

    for dx, dy in DIRS:
        nx, ny = x+dx, y+dy
        if in_bounds(nx, ny):
            if (nx, ny) in pits:
                breeze = True
            if (nx, ny) == wumpus:
                stench = True

    return breeze, stench

def infer(x, y):
    global inference_steps
    inference_steps += 1

    breeze, stench = get_percepts(x,y)

    if not breeze and not stench:
        for dx, dy in DIRS:
            nx, ny = x+dx, y+dy
            if in_bounds(nx, ny):
                safe_cells.add((nx, ny))

def simulate():
    global agent_pos

    steps = []
    stack = [agent_pos]   # acts like DFS exploration
    visited_set = set()   

    while stack:
        x, y = stack.pop()

        if (x, y) in visited_set:
            continue

        visited_set.add((x, y))
        agent_pos = (x, y)

        infer(x, y)
        breeze, stench = get_percepts(x, y)

        steps.append({
            "agent": (x, y),
            "visited": list(visited_set),
            "safe": list(safe_cells),
            "breeze": breeze,
            "stench": stench,
            "pits": list(pits),
            "wumpus": wumpus
        })

        # explore neighbors
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            if in_bounds(nx, ny) and (nx, ny) not in visited_set:
                if (nx, ny) in safe_cells:
                    stack.append((nx, ny))

    visited[:] = list(visited_set)  # Update global visited list
    return steps

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    global size, wumpus, inference_steps

    size_input = int(request.json["size"])

    if size_input < 4 or size_input > 20:
        return jsonify({"error": "Invalid grid size"}), 400

    size = size_input
    wumpus = generate_world(size)
    inference_steps = 0

    return jsonify({"status": "ok"})

@app.route("/run")
def run():
    steps = simulate()

    return jsonify({
        "steps": steps,
        "inference": inference_steps,
        "visited": visited
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)