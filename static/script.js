let size;
let steps = [];

function generateGrid() {
    size = parseInt(document.getElementById("size").value);

    const error = document.getElementById("error");

if (isNaN(size) || size < 4 || size > 20) {
    error.innerText = "Grid size must be between 4 and 20";
    return;
} else {
    error.innerText = "";
}

    fetch("/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({size: size})
    });

    drawEmptyGrid();
    document.getElementById("runBtn").disabled = false;
}

function drawEmptyGrid() {
    const grid = document.getElementById("grid");
    grid.style.gridTemplateColumns = `repeat(${size}, 60px)`;
    grid.innerHTML = "";

    for (let i = 0; i < size * size; i++) {
        let cell = document.createElement("div");
        cell.classList.add("cell");
        grid.appendChild(cell);
    }
}

function drawStep(step) {
    const grid = document.getElementById("grid");
    const cells = grid.children;

    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            let index = i * size + j;
            let cell = cells[index];
            cell.className = "cell";
            cell.innerHTML = "";

            let pos = [i,j].toString();

            if (step.safe.some(c => c.toString() === pos)) {
                cell.classList.add("safe");
            }

            if (step.pits.some(c => c.toString() === pos)) {
                cell.classList.add("pit");
                cell.innerHTML = "🕳";
            }

            if (step.wumpus.toString() === pos) {
                cell.classList.add("wumpus");
                cell.innerHTML = "👹";
            }

            if (step.agent.toString() === pos) {
                cell.classList.add("agent");

                if (step.breeze) cell.innerHTML += "🌬";
                if (step.stench) cell.innerHTML += "💨";
                cell.innerHTML += "🤖";
            }
        }
    }
}

let isRunning = false;

async function runSimulation() {
    if (isRunning) return;

    isRunning = true;

    let res = await fetch("/run");
    let data = await res.json();

    animateSteps(data.steps, data);

    setTimeout(() => {
        isRunning = false;
    }, data.steps.length * 600);
}

function animateSteps(steps, data) {
    let i = 0;

    function nextStep() {
        if (i >= steps.length) {
            // show stats at end
            document.getElementById("stats").classList.remove("hidden");
            document.getElementById("inf").innerText = data.inference;
            document.getElementById("vis").innerText = data.visited.length;
            return;
        }

        drawStep(steps[i]);
        i++;

        setTimeout(nextStep, 600); // smoother than setInterval
    }

    nextStep();
}