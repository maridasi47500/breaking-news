  

var theme = 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png';
    var lat = 8.619543;
        var lon = 0.82;
            var alt =481;
                var macarte = null;
                    //var trace = new Array();
                        var i = 0;
                            //var marker1;
                                var markerClusters; // Servira à stocker les groupes de marqueurs
                                    var popup = L.popup();
                                      function initMap(){

                                            // Nous définissons le dossier qui contiendra les marqueurs
                                                  //var iconBase = 'img';
                                                        // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
                                                              macarte = L.map('map').setView([lat, lon], 5);

                                                                    markerClusters = L.markerClusterGroup; // Nous initialisons les groupes de marqueurs
                                                                          // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
                                                                                L.tileLayer(theme, {
                                                                                          // Il est toujours bien de laisser le lien vers la source des données
                                                                                                    //attribution: 'données © OpenStreetMap/ODbL - rendu OSM France',
                                                                                                              minZoom: 1,
                                                                                                                        maxZoom: 20
                                                                                                                              }).addTo(macarte);
                                                                                                                                    macarte.on('click', onMapClick);
                                                                                                                                      }


   function onMapClick(e) {
           var mylat = document.getElementById("lat");
           var mylon = document.getElementById("lon");
	   if (document.getElementById("lat") && document.getElementById("lon")){
	       popup
	           .setLatLng(e.latlng)
	           .setContent("You clicked the map at " + e.latlng.toString())
	           .openOn(macarte);
	       var marker = L.marker(e.latlng).addTo(macarte)
	       mylat.value=e.latlng.lat;
	       mylon.value=e.latlng.lng;
	   }
   }




                                                                                                                                                                                                      $(document).ready(function(){
                                                                                                                                                                                                              initMap();
                                              if (window.location.href==="/"){
}
                                                                                                                                                                                                                  });
