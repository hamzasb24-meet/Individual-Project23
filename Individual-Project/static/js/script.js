const birdData = {
  bird1: {
    name: 'Bird 1',
    description: 'Information about Bird 1...',
  },
  bird2: {
    name: 'Bird 2',
    description: 'Information about Bird 2...',
  },
  // Add more bird data as needed
};

function showBirdInfo(birdId) {
  const birdInfo = document.getElementById('birdInfo');
  const birdNameElement = document.getElementById('birdName');
  const birdDescriptionElement = document.getElementById('birdDescription');

  if (birdData[birdId]) {
    birdNameElement.textContent = birdData[birdId].name;
    birdDescriptionElement.textContent = birdData[birdId].description;
    birdInfo.style.display = 'block';
  } else {
    birdInfo.style.display = 'none';
  }
}

const searchBox = document.getElementById('searchBox');
searchBox.addEventListener('input', function () {
  const searchTerm = searchBox.value.toLowerCase();
  const birds = document.querySelectorAll('.bird');

  birds.forEach((bird) => {
    const birdName = bird.getElementsByTagName('img')[0].alt.toLowerCase();
    if (birdName.includes(searchTerm)) {
      bird.style.display = 'block';
    } else {
      bird.style.display = 'none';
    }
  });
});
