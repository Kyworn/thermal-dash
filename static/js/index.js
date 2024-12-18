// Temperature history for graphing
const cpuTemperatureHistory = [];
const gpuTemperatureHistory = [];
const chartMaxLength = 30;  // Keep last 30 data points

// Chart configuration
const ctx = document.getElementById('temperature-chart').getContext('2d');
const temperatureChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Array(chartMaxLength).fill(''),  // Create empty labels
        datasets: [
            {
                label: 'CPU',
                data: cpuTemperatureHistory,
                borderColor: 'rgb(75, 192, 192)',
                borderWidth: 2,
                pointRadius: 0,
                tension: 0.4,
                fill: false
            },
            {
                label: 'GPU',
                data: gpuTemperatureHistory,
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 2,
                pointRadius: 0,
                tension: 0.4,
                fill: false
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: false,
                min: 30,  // Start y-axis at a reasonable temperature
                max: 90,  // Max temperature
                ticks: {
                    stepSize: 10
                },
                grid: {
                    color: 'rgba(255,255,255,0.1)'
                }
            },
            x: {
                display: false  // Hide x-axis labels
            }
        },
        plugins: {
            legend: {
                display: true,
                labels: {
                    color: 'white',
                    font: {
                        size: 10
                    }
                },
                position: 'top'
            }
        },
        animation: {
            duration: 0  // Disable animations
        }
    }
});

function fetchTemperatures() {
    fetch('/temperatures')
        .then(response => response.json())
        .then(data => {
            const cpuTemp = data.cpu || 'N/A';
            const gpuTemp = data.gpu || 'N/A';

            // Update temperature text
            document.getElementById('cpu-temp').textContent = cpuTemp;
            document.getElementById('gpu-temp').textContent = gpuTemp;

            // Update temperature graph
            if (typeof cpuTemp === 'number') {
                // Add new temperatures to history
                cpuTemperatureHistory.push(cpuTemp);

                // Limit history length
                if (cpuTemperatureHistory.length > chartMaxLength) {
                    cpuTemperatureHistory.shift();
                }

                // Ensure the chart always has the full number of points
                while (cpuTemperatureHistory.length < chartMaxLength) {
                    cpuTemperatureHistory.unshift(cpuTemp);
                }
            }

            if (typeof gpuTemp === 'number') {
                // Add new temperatures to history
                gpuTemperatureHistory.push(gpuTemp);

                // Limit history length
                if (gpuTemperatureHistory.length > chartMaxLength) {
                    gpuTemperatureHistory.shift();
                }

                // Ensure the chart always has the full number of points
                while (gpuTemperatureHistory.length < chartMaxLength) {
                    gpuTemperatureHistory.unshift(gpuTemp);
                }
            }

            // Update chart
            temperatureChart.update('none');
        })
        .catch(error => {
            console.error('Error fetching temperatures:', error);
        });
}

// Initial temperature fetch and set up periodic updates
fetchTemperatures();
setInterval(fetchTemperatures, 200);
