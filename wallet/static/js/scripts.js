// Transaction History Chart
const transactionCtx = document.getElementById('transactionHistoryChart').getContext('2d');
const transactionHistoryChart = new Chart(transactionCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [{
            label: 'Transactions',
            data: [1100, 1300, 1500],
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                max: 2000
            },
            x: {
                beginAtZero: true
            }
        }
    }
});

// Statistics Chart
const statisticsCtx = document.getElementById('statisticsChart').getContext('2d');
const statisticsChart = new Chart(statisticsCtx, {
    type: 'doughnut',
    data: {
        labels: ['Spent', 'Received'],
        datasets: [{
            data: [5000, 2500],
            backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)']
        }]
    },
    options: {
        responsive: true,
        cutoutPercentage: 70
    }
});
