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
                //            return this.readyState;
                }
}

var lat;
var lag;
var map;
var marker;
var latii;
var lngii;


