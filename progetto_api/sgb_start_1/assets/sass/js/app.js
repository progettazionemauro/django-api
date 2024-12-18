async function fetchColors() {
    try {
      const response = await fetch('https://www.colourlovers.com/api/colors/new?format=json');
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching colors:', error);
      return [];
    }
  }
  
  async function renderColors() {
    const colorsData = await fetchColors();
    const appContainer = document.getElementById('app');
  
    colorsData.forEach(item => {
      const colorElement = document.createElement('div');
      colorElement.classList.add('color'); // Add a class for styling if needed
      colorElement.innerHTML = `
        <h1>${item.title}</h1>
        <p>ID: ${item.id}</p>
        <p>Description: ${item.description}</p>
        <p>URL: <a href="${item.url}">${item.url}</a></p>
      `;
      appContainer.appendChild(colorElement);
    });
  }
  
  renderColors();
  