// Create a new map object
const map = L.map('map').setView([46.2276, 2.2137], 6);

for(let i in departments.features) {
    let code = parseInt(departments.features[i].properties.code);
    for(let j in external_data.deps) {
        if(code == external_data.deps[j].departement) {
            departments.features[i].properties.crimeRate = external_data.deps[j].taux_criminalite;
            departments.features[i].properties.electionResult = external_data.deps[j].gagnant;
        }
    }
}

function getMinValue() {
    return external_data.deps.reduce((min, p) => p.taux_criminalite < min ? p.taux_criminalite : min, external_data.deps[0].taux_criminalite);
}

function getMaxValue() {
    return external_data.deps.reduce((max, p) => p.taux_criminalite > max ? p.taux_criminalite : max, external_data.deps[0].taux_criminalite);
}

// Get color depending on the value of the crime rate
function getColor(d) {
    let max = getMaxValue();
    let min = getMinValue();
    let diff = max - min;
    let step = diff / 5;
    return d > min + step * 4 ? '#800026' :
              d > min + step * 3  ? '#BD0026' :
                d > min + step * 2  ? '#E31A1C' :
                    d > min + step  ? '#FC4E2A' :
                        '#FD8D3C';

}

function style(feature) {
    return {
    	fillColor: getColor(feature.properties.crimeRate),
	    weight: 2,
	    opacity: 1,
	    color: 'white',
	    dashArray: '3',
	    fillOpacity: 1
    }
};

// function to get percentage from ratio with the precision as a parameter
function getPercentage(ratio, precision=8) {
    return (ratio * 100).toFixed(precision);
}

function popup(feature, layer) {
	layer.bindPopup(feature.properties.nom+", "+feature.properties.code+"</br>"+getPercentage(feature.properties.crimeRate)+"% de criminalite</br>"+feature.properties.electionResult);
}

// Map layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// GeoJSON layer with style and popup
geojson = L.geoJson(departments, {style: style, onEachFeature: popup}).addTo(map);