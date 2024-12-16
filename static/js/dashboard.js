async function fetchAgeDistribution() {
    const response = await fetch('/statistics/age');
    const data = await response.json();
    const labels = data.age_distribution.map((_, i) => `Age Group ${i + 1}`);
    const chartData = {
        labels: labels,
        datasets: [{
            label: 'Age Distribution',
            data: data.age_distribution,
            borderWidth: 1
        }]
    };

    const ctx = document.getElementById('ageChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: chartData,
    });
}

async function fetchDeathCauses() {
    const response = await fetch('/statistics/deaths');
    const data = await response.json();
    const labels = Object.keys(data);
    const chartData = {
        labels: labels,
        datasets: [{
            label: 'Death Causes',
            data: Object.values(data),
            borderWidth: 1
        }]
    };

    const ctx = document.getElementById('deathChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: chartData,
    });
}

fetchAgeDistribution();
fetchDeathCauses();
