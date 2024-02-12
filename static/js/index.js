const itemReportedChart = document.getElementById("item-reported");
const totalossChart = document.getElementById("total-loss");
const totalfoundChart = document.getElementById("total-found");
const totalitems = document.getElementById("total");
const overview = document.getElementById("summary");
const datatable = document.getElementById("datatable");

fetch("/reportitem")
    .then(res => res.json())
    .then(data => console.log(data))
new Chart(itemReportedChart, {
    type: 'line',
    data: {
        labels: data.labels,
        datasets: [{
            label: '#total votes',
            data: data.data,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const itemlostChart = new Chart(totalossChart, {
    type: 'line',
    data: {
        labels: ['Electronics', 'Stationary'],
        datasets: [{
            label: '#total votes',
            data: [500, 2502],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }

});
const foundChart = new Chart(totalfoundChart, {
    type: 'line',
    data: {
        labels: ['Electronics', 'Stationary'],
        datasets: [{
            label: '#total votes',
            data: [500, 2502],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const total = new Chart(totalitems, {
    type: 'line',
    data: {
        labels: ['Electronics', 'Stationary'],
        datasets: [{
            label: '#total votes',
            data: [500, 2502],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const overviewChart = new Chart(overview, {
    type: 'pie',
    data: {
        labels: [
            'Red',
            'Blue',
            'Yellow'
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 50, 100],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ]
        }]

    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }

})