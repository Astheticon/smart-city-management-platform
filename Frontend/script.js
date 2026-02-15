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

// Update prediction display
function updatePrediction(data) {
    const predictionDiv = document.getElementById("prediction");

    if (!data || !data.prediction) {
        predictionDiv.innerHTML = "<strong>Traffic Congestion Level:</strong> N/A";
        return;
    }

    const level = data.prediction.traffic_congestion_level;

    predictionDiv.innerHTML = `
        <strong>Traffic Congestion Level:</strong> 
        <span style="font-size: 20px; font-weight: bold;">
            ${level}
        </span>
    `;
}

// Update alerts panel
function updateAlerts(alerts) {
    const container = document.getElementById("alerts");
    container.innerHTML = "";

    if (!alerts || alerts.length === 0) {
        container.innerHTML = "<p>No recent alerts</p>";
        return;
    }

    alerts.forEach(alert => {
        const div = document.createElement("div");
        div.classList.add("alert");

        if (alert.priority === "HIGH") div.classList.add("high");
        if (alert.priority === "MEDIUM") div.classList.add("medium");
        if (alert.priority === "LOW") div.classList.add("low");

        div.innerHTML = `
            <strong>${alert.alert_type}</strong><br>
            ${alert.message}<br>
            <small>${alert.timestamp}</small>
        `;

        container.appendChild(div);
    });
}

// Refresh all dashboard data
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
