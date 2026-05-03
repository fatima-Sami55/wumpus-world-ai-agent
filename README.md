# 🧠 Dynamic Wumpus World – Knowledge-Based AI Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black.svg)
![AI](https://img.shields.io/badge/AI-Knowledge%20Based-green.svg)
![Logic](https://img.shields.io/badge/Propositional%20Logic-Inference-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## 📌 Overview

This project is a **web-based intelligent agent simulation** of the classic **Wumpus World problem**.  
The agent operates in a dynamically generated grid, uses **propositional logic**, and performs **percept-based reasoning** to safely explore the environment.

It is built using **Flask (Python backend)** and a **modern interactive frontend UI**.

---

## 🎯 Key Features

- 🔲 Dynamic grid size (4×4 to 20×20)
- 👹 Random Wumpus placement
- 🕳 Random Pit generation
- 🌬 Breeze detection (adjacent pits)
- 💨 Stench detection (adjacent Wumpus)
- 🧠 Knowledge-based reasoning (safe cell inference)
- 🤖 Automated agent execution (single click run)
- 🎞 Smooth step-by-step animation
- 📊 Live metrics dashboard (inference steps + visited cells)
- 🎨 Modern interactive UI with icons

---

## 🧠 AI Logic

The agent follows a simplified **Knowledge-Based Agent model**:

- Percepts are added to the Knowledge Base
- Rules are inferred using propositional logic
- Safe cells are deduced when:
  - No Breeze → no adjacent pits
  - No Stench → no adjacent Wumpus
- Agent only moves into **logically safe cells**

---

## 🏗️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Logic:** Propositional inference (simplified KB model)
- **Visualization:** Grid-based animated UI

---

## 🚀 How to Run

### 1. Clone repository
```bash
git clone https://github.com/your-username/wumpus-world-logic-agent.git
cd wumpus-world-logic-agent
```

### 2. Install dependencies
```bash
pip install flask
```

### 3. Run the app
```bash
python app.py
```

###  4. Open in browser
```bash
http://127.0.0.1:5000
```


## 🎮 How to Use

1. Enter grid size (4–20)  
2. Click **Generate Grid**  
3. Click **Start Execution**  
4. Watch the AI agent explore safely step-by-step  
5. View final statistics after completion  

---

## 📊 Output Metrics

At the end of execution, the system displays:

- Total inference steps  
- Number of visited cells  
- Safe exploration path  
- Percept-based decision behavior  

---

## 📷 Visual Elements

- 🤖 Agent → current position  
- 🟩 Safe cells → green highlight  
- 🕳 Pit → danger zone  
- 👹 Wumpus → lethal hazard  
- 🌬 Breeze → nearby pit indicator  
- 💨 Stench → nearby Wumpus indicator  

---

## 💡 Learning Outcomes

This project demonstrates:

- Knowledge-Based Agents (AI concept)  
- Propositional Logic reasoning  
- Percept-driven decision making  
- Graph/grid traversal logic  
- Real-time web visualization  

---

## 📌 Future Improvements

- Full CNF + Resolution engine  
- Probabilistic Wumpus inference  
- Optimal pathfinding (A* integration)  
- Multi-agent simulation  
- Replay system for executions  

---

## 👨‍💻 Author

Developed as an academic AI project demonstrating intelligent agent design in a dynamic environment.

---

## ⭐ Support

If you like this project, consider giving it a star!