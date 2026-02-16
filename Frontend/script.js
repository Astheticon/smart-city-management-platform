const API_BASE = "http://127.0.0.1:8000";

// Fetch latest sensor data
async function fetchLatest() {
    const response = await fetch(`${API_BASE}/latest`);
    return await response.json();
}

// Fetch recent alerts
async function fetchAlerts() {
    const response = await fetch(`${API_BASE}/alerts?limit=5`);
    return await response.json();
}

// Update dashboard cards
function updateDashboard(data) {
    if (!data || data.message) return;

    document.getElementById("vehicleCount").innerText = data.vehicle_count ?? "--";
    document.getElementById("aqi").innerText = data.aqi ?? "--";
    document.getElementById("temperature").innerText = data.temperature ?? "--";
    document.getElementById("humidity").innerText = data.humidity ?? "--";
    document.getElementById("trafficDensity").innerText = data.traffic_density ?? "--";
}

// Update prediction
function updatePrediction(data) {
    const predictionDiv = document.getElementById("prediction");

    if (!data || data.traffic_density == null) {
        predictionDiv.className = "prediction";
        predictionDiv.innerText = "N/A";
        return;
    }

    const density = data.traffic_density;
    let level = "LOW";

    if (density < 40) {
        level = "LOW";
    } else if (density < 70) {
        level = "MEDIUM";
    } else {
        level = "HIGH";
    }

    predictionDiv.className = "prediction";
    predictionDiv.classList.add(level.toLowerCase());
    predictionDiv.innerText = level;
}

// Update alerts
function updateAlerts(alerts) {
    const container = document.getElementById("alerts");
    container.innerHTML = "";

    if (!alerts || alerts.length === 0) {
        container.innerHTML = "<p>No recent alerts</p>";
        return;
    }

    alerts.forEach(alert => {
        const div = document.createElement("div");
        div.className = "alert-card";

        if (alert.priority === "HIGH") {
            div.classList.add("alert-high");
        } else if (alert.priority === "MEDIUM") {
            div.classList.add("alert-medium");
        } else {
            div.classList.add("alert-low");
        }

        div.innerHTML = `
            <strong>${alert.alert_type}</strong><br>
            ${alert.message}<br>
            <small>${alert.timestamp ?? ""}</small>
        `;

        container.appendChild(div);
    });
}

// Refresh dashboard
async function refreshData() {
    try {
        const latest = await fetchLatest();
        const alerts = await fetchAlerts();

        updateDashboard(latest);
        updatePrediction(latest);
        updateAlerts(alerts);

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Auto refresh every 3 seconds
setInterval(refreshData, 3000);

// Initial load
refreshData();
