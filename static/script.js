// Function to fetch and display data
async function fetchAndDisplayData() {
    try {
        const response = await fetch("/city-data");
        const data = await response.json();

        const resultDiv = document.getElementById("result");
        const { data: metrics, actions } = data;

        let resultHTML = "<h2>City Metrics</h2><ul>";
        for (const [key, value] of Object.entries(metrics)) {
            resultHTML += `<li>${key.replace("_", " ").toUpperCase()}: ${value}</li>`;
        }
        resultHTML += "</ul><h2>Recommended Actions</h2><ul>";
        for (const [domain, action] of Object.entries(actions)) {
            resultHTML += `<li>${domain.replace("_", " ").toUpperCase()}: ${action}</li>`;
        }
        resultHTML += "</ul>";

        resultDiv.innerHTML = resultHTML;
    } catch (error) {
        console.error("Error fetching data:", error);
        document.getElementById("result").innerHTML = "<p>Error loading data.</p>";
    }
}

// Automatically fetch and display data when the page loads
window.addEventListener("DOMContentLoaded", fetchAndDisplayData);

// Fetch and display new data when the button is clicked
document.getElementById("fetchNewData").addEventListener("click", fetchAndDisplayData);