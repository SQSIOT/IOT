<html>
<head>
  <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map-canvas { height: 100% }
    </style>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Live Viewer</title>  	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="//maps.googleapis.com/maps/api/js?key=AIzaSyBurRieu1eJUOxP0KScUILO2C37ydTNV_U&callback=initialise" async="" defer="defer" type="text/javascript"></script>

 <script>

 function showHint(str) {
	var newurl;
	var textval;
	
    if (str.length == 0) {
       //document.getElementById("txtHint").innerHTML = "";
        return;
    } 
	else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
				textval = this.responseText;
            }
        };
		newurl = "aaa.php?q=" + str;
        xmlhttp.open("GET", newurl, false);
        xmlhttp.send();
		return textval;		
	//	return this.readyState;
	}
 }
 
var lat;
var lag;
var map;
var marker;
var  lat1 = parseFloat('18.591819');
var  lon1 = parseFloat('73.688892');
var flag  = 0;
var flag1 = 0; 

//var lat2 = '18.597384';
//var lon2 = '73.718863';

//console.log("Lat1 is:",lat1);
//console.log("Lon1 is:",lon1);

function initialise() {
  lag = showHint('longi');
  lat = showHint('lati');
  
  var myLatlng = new google.maps.LatLng(lat, lag);
    	
  var mapOptions = {
    zoom: 13,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
  });
     
    marker.setMap( map );	
//	moveMarker( map, marker );
}


function moveMarker( map, marker ) {

	lag = showHint('longi');
	lat = showHint('lati');
  
	var myLatlng = new google.maps.LatLng(lat, lag);
	var d;	
	setTimeout( function(){
		marker.setPosition(new google.maps.LatLng(lat, lag));
		map.panTo(new google.maps.LatLng(lat, lag));       	
	}, 1000);
	var lat2 = lat;
	var lon2 = lag;
//	console.log("Lat2 is:",lat2);
//	console.log("Lon2 is:",lon2);

	
	d = distance(lat1,lon1,lat2,lon2);
//console.log(lat);	
	console.log("distance is:",d);
	
	
	
	if( d <= '350m' ){
		flag = 1
	}
	
	else if(d > '350m') {
		flag = 0
	}
	
	console.log("Flag is",flag,flag1)
	
	if (flag == 0 && flag1 == 0){
		//LEDOFF
		var mywindow = window.open("https://clda.sqs.com/home/test.php?value=LED1=OFF","mywindow", "location=1,status=1,scrollbars=1,  width=100,height=100");
			//mywindow.moveTo(0, 0);
			console.log("LED is OFF")
		flag1 = 1;
	}
	
	else if(flag == 1 && flag1 == 1){
		//LEDOFN
		 var mywindow = window.open("https://clda.sqs.com/home/test.php?value=LED1=ON","mywindow", "location=1,status=1,scrollbars=1,  width=100,height=100");
		 //mywindow.moveTo(0, 0);
		 console.log("LED is ON")
		flag1 = 0;
	}
		
		
		/*{
			 
		
		 var mywindow = window.open("https://clda.sqs.com/home/test.php?value=LED1=ON","mywindow", "location=1,status=1,scrollbars=1,  width=100,height=100");
		 mywindow.moveTo(0, 0);
		 console.log("LED is ON")
		 flag = 1;		
		}
		
		else if (d >= '300m' && flag === 1)
		{
			var mywindow = window.open("https://clda.sqs.com/home/test.php?value=LED1=OFF","mywindow", "location=1,status=1,scrollbars=1,  width=100,height=100");
			mywindow.moveTo(0, 0);
			console.log("LED is OFF")
			flag = 0;
		}*/
};



function distance(lat1,lon1,lat2,lon2) {
	

	var R = 6371; // km (change this constant to get miles)
	var dLat = (lat2-lat1) * Math.PI / 180;
	var dLon = (lon2-lon1) * Math.PI / 180;
	var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
		Math.cos(lat1 * Math.PI / 180 ) * Math.cos(lat2 * Math.PI / 180 ) *
		Math.sin(dLon/2) * Math.sin(dLon/2);
	
	var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
//	console.log("R is:",R);
//	console.log("DLAT:",dLat);
//	console.log("DLON is:",dLon);
//	console.log("A is:",a);
//	console.log("C is:",c);
	var d = R * c;
//	console.log("distance is:",d);

	if (d>1)
		return Math.round(d)+"km";
	
	else if (d<=1)
		return Math.round(d*1000)+"m";
	return d;
	
	

	
}


  
setInterval(function(){moveMarker( map, marker )},8000);
google.maps.event.addDomListener(window, 'load', initialise);

 </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
 </html>