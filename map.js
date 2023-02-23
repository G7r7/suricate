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

function getColor(d) {
	return d > 8? '#800026' :
        d > 6 ? '#C70039' :
        d > 4 ? '#EE4F4F' :
        d > 2 ? '#EEAD4F' :
        '#EBCE17';
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

function popup(feature, layer) {
	layer.bindPopup(feature.properties.nom+", "+feature.properties.code+"</br>"+feature.properties.crimeRate+"% de criminalite</br>"+feature.properties.electionResult);
}

// Map layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// GeoJSON layer with style and popup
geojson = L.geoJson(departments, {style: style, onEachFeature: popup}).addTo(map);