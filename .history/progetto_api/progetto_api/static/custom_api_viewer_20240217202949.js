// JavaScript code to fetch data from the DRF API and update the HTML content
fetch('http://127.0.0.1:8082/django_api_for_wagtail/nations/')
    .then(response => response.json())
    .then(data => {
        // Update the HTML content with the API data
        document.getElementById('api-data').innerHTML = JSON.stringify(data);
    })
    .catch(error => console.error('Error fetching data:', error));
