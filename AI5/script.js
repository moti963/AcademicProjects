


let obstacle = [];
const grid = document.getElementById('grid');
const random = document.getElementById("range").value;
grid.addEventListener('click', (e) => {
    let elementId = e.target.id;
    console.log(elementId)
    if (elementId != 'grid') {
        if (elementId !== '') {

            obstacle.push({ x: parseInt(elementId.split('-')[0]), y: parseInt(elementId.split('-')[1]) });
            document.getElementById(elementId).classList.add('obstacle');
        }
        else {
            console.log("An element without an id was clicked.");
        }
    }
}
);
function reload() {
    location.reload();
}
function generate() {
    document.getElementById("generate").disabled = true;
    const gridSize = { rows: document.getElementById("rows").value, cols: document.getElementById("column").value };
    const start = { x: document.getElementById("startx").value, y: document.getElementById("starty").value };
    const end = { x: document.getElementById("endx").value, y: document.getElementById("endy").value };
    const grid = document.getElementById('grid');


    if (parseInt(start.x) >= parseInt(gridSize.cols) || parseInt(start.y) >= parseInt(gridSize.rows) || parseInt(end.x) >= parseInt(gridSize.cols) || parseInt(end.y) >= parseInt(gridSize.rows)) {
        alert("out of bound");
        location.reload();
    }

    else if (start.x == end.x && start.y == end.y) {
        alert("start and end cannot be same");
        location.reload();
    }

    else {

        for (let i = 0; i < gridSize.rows; i++) {
            const row = document.createElement('tr');
            for (let j = 0; j < gridSize.cols; j++) {
                const cell = document.createElement('td');
                const cellId = i + '-' + j;
                cell.setAttribute('id', cellId);
                row.appendChild(cell);
            }
            grid.appendChild(row);
        }
        document.getElementById(`${start.x}-${start.y}`).classList.add('start');
        document.getElementById(`${start.x}-${start.y}`).innerHTML = 'start';
        document.getElementById(`${end.x}-${end.y}`).classList.add('end');
        document.getElementById(`${end.x}-${end.y}`).innerHTML = 'end';
        let count = document.getElementById("range").value
        for (let index = 0; index < count; index++) {
            let rax = Math.floor(Math.random() * gridSize.cols)
            let ray = Math.floor(Math.random() * gridSize.rows)
            obstacle.push({ x: rax, y: ray });
            console.log(`${rax}-${ray}`)
            document.getElementById(`${rax}-${ray}`).classList.add('obstacle');
        }
    }
}
function path() {
    const path = document.getElementsByClassName('path');
    while (path.length > 0) {
        path[0].classList.remove('path');
    }
    const start = { x: parseInt(document.getElementById("startx").value), y: parseInt(document.getElementById("starty").value) };
    const end = { x: parseInt(document.getElementById("endx").value), y: parseInt(document.getElementById("endy").value) };
    console.log(obstacle);
    const pathFound = findPath(start, end, obstacle);
    if (pathFound.length > 0) {
        for (const point of pathFound) {
            document.getElementById(`${point.x}-${point.y}`).classList.add('path');
        }
    } else {
        alert('No valid path found from the current mouse position to the end point!');
    }
};
function findPath(start, end, obstacles) {
    const queue = [];
    const visited = new Set();
    const parent = new Map();

    queue.push(start);
    visited.add(`${start.x}-${start.y}`);

    while (queue.length > 0) {
        const current = queue.shift();
        if (current.x === end.x && current.y === end.y) {
            return reconstructPath(parent, current);
        }
        const neighbors = generateNeighbors(current, obstacles, visited);

        for (const neighbor of neighbors) {
            queue.push(neighbor);
            visited.add(`${neighbor.x}-${neighbor.y}`);
            parent.set(`${neighbor.x}-${neighbor.y}`, current);
        }
    }

    return [];
}
function generateNeighbors(point, obstacles, visited) {
    const gridSize = { rows: document.getElementById("rows").value, cols: document.getElementById("column").value };
    const neighbors = [];
    const directions = [
        { x: -1, y: 0 },
        { x: 1, y: 0 },
        { x: 0, y: -1 },
        { x: 0, y: 1 }
    ];

    for (const direction of directions) {
        const neighborX = point.x + direction.x;
        const neighborY = point.y + direction.y;
        if (neighborX >= 0 && neighborX < gridSize.rows && neighborY >= 0 && neighborY < gridSize.cols) {
            const neighbor = { x: neighborX, y: neighborY };
            if (!isObstacle(neighbor, obstacles) && !visited.has(`${neighbor.x}-${neighbor.y}`)) {
                neighbors.push(neighbor);
            }
        }
    }

    return neighbors;
}

function isObstacle(point, obstacles) {
    for (const obstacle of obstacles) {
        if (point.x === obstacle.x && point.y === obstacle.y) {
            return true;
        }
    }

    return false;
}

function reconstructPath(parent, current) {
    const path = [];
    while (current) {
        path.push(current);
        current = parent.get(`${current.x}-${current.y}`);
    }
    path.reverse();
    return path;
}