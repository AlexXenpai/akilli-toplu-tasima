const API_URL = "http://localhost:5000/api";

const canvas = document.getElementById("mapCanvas");
const ctx = canvas.getContext("2d");

let stops = [];
let connections = [];
let selectedPoint = null;
let nearestStops = [];
let routePath = [];

async function init() {
    stops = await fetch(`${API_URL}/stops`).then(response => response.json());
    connections = await fetch(`${API_URL}/connections`).then(response => response.json());

    fillStopSelects();
    drawMap();
}

function fillStopSelects() {
    const startSelect = document.getElementById("startStop");
    const targetSelect = document.getElementById("targetStop");

    stops.forEach(stop => {
        const startOption = document.createElement("option");
        startOption.value = stop.id;
        startOption.textContent = stop.name;

        const targetOption = document.createElement("option");
        targetOption.value = stop.id;
        targetOption.textContent = stop.name;

        startSelect.appendChild(startOption);
        targetSelect.appendChild(targetOption);
    });

    if (stops.length > 1) {
        targetSelect.selectedIndex = 1;
    }
}

function getStopById(id) {
    return stops.find(stop => stop.id === id);
}

function drawMap() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawConnections();
    drawRoute();
    drawStops();
    drawSelectedPoint();
}

function drawConnections() {
    ctx.lineWidth = 2;
    ctx.strokeStyle = "#94a3b8";
    ctx.fillStyle = "#475569";
    ctx.font = "12px Arial";

    connections.forEach(connection => {
        const from = getStopById(connection.from);
        const to = getStopById(connection.to);

        ctx.beginPath();
        ctx.moveTo(from.x, from.y);
        ctx.lineTo(to.x, to.y);
        ctx.stroke();

        const midX = (from.x + to.x) / 2;
        const midY = (from.y + to.y) / 2;
        ctx.fillText(`${connection.line} / ${connection.time} dk`, midX + 4, midY - 4);
    });
}

function drawRoute() {
    if (routePath.length < 2) {
        return;
    }

    ctx.strokeStyle = "#16a34a";
    ctx.lineWidth = 6;
    ctx.beginPath();

    routePath.forEach((stop, index) => {
        if (index === 0) {
            ctx.moveTo(stop.x, stop.y);
        } else {
            ctx.lineTo(stop.x, stop.y);
        }
    });

    ctx.stroke();
}

function drawStops() {
    stops.forEach(stop => {
        let color = "#2563eb";

        if (nearestStops.some(item => item.id === stop.id)) {
            color = "#f59e0b";
        }

        if (routePath.some(item => item.id === stop.id)) {
            color = "#16a34a";
        }

        ctx.beginPath();
        ctx.arc(stop.x, stop.y, 11, 0, Math.PI * 2);
        ctx.fillStyle = color;
        ctx.fill();

        ctx.fillStyle = "#111827";
        ctx.font = "13px Arial";
        ctx.fillText(stop.name, stop.x + 15, stop.y + 5);
    });
}

function drawSelectedPoint() {
    if (!selectedPoint) {
        return;
    }

    ctx.beginPath();
    ctx.arc(selectedPoint.x, selectedPoint.y, 8, 0, Math.PI * 2);
    ctx.fillStyle = "#dc2626";
    ctx.fill();

    ctx.fillStyle = "#111827";
    ctx.font = "13px Arial";
    ctx.fillText("Kullanıcı", selectedPoint.x + 12, selectedPoint.y + 4);
}

canvas.addEventListener("click", async event => {
    const rect = canvas.getBoundingClientRect();

    selectedPoint = {
        x: Math.round((event.clientX - rect.left) * (canvas.width / rect.width)),
        y: Math.round((event.clientY - rect.top) * (canvas.height / rect.height))
    };

    const k = document.getElementById("kValue").value;

    nearestStops = await fetch(`${API_URL}/nearest`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            x: selectedPoint.x,
            y: selectedPoint.y,
            k: k
        })
    }).then(response => response.json());

    document.getElementById("nearestResult").innerHTML = nearestStops.map(stop => `
        <div class="result-item">
            <strong>${stop.name}</strong><br>
            Kullanıcıya uzaklık: ${stop.distanceToUser}
        </div>
    `).join("");

    drawMap();
});

async function findRoute() {
    const start = document.getElementById("startStop").value;
    const target = document.getElementById("targetStop").value;

    const result = await fetch(`${API_URL}/route`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            start: start,
            target: target
        })
    }).then(response => response.json());

    routePath = result.pathStops;

    document.getElementById("routeResult").innerHTML = `
        <div class="result-item">
            <strong>Toplam süre:</strong> ${result.totalCost} dakika<br>
            <strong>Rota:</strong> ${routePath.map(stop => stop.name).join(" → ")}
        </div>
    `;

    drawMap();
}

init();