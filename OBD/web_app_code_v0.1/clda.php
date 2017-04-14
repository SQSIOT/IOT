<?php
session_start();
if(empty($_SESSION['login_user']))
{
	header("Location: index.php");
}
?>
<html>
  <head>
   <style>
.city {
   float: left;
  margin: 10px;
  padding: 20px;
   max-width: 150px;
   height: 200px;
  // border: 1px solid black;
   display: inline-block;
} 
.after-box {
	float: left;
	padding: 10px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 220px;
  height: 220px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 350%;
  position: relative;
  box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 1%;
border: 6px solid black;  
}
.after-box0 {
	float: left;
	padding: 10px;
	background-color: red;
    clear: left;
    border: 3px solid red;   
	height: 220px;
  width: 220px;
  border-radius: 50%;
  text-align: center;
  color: red;
  text-shadow: 3px 2px yellow;
  vertical-align: middle;
  font-size: 350%;
  position: relative;
  box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 1%;	
  border: 6px solid black;  
}  
.after-box1 {
	float: left;
	padding: 10px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 220px;
  height: 220px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 350%;
  position: relative;
  box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 1%;
border: 6px solid black;  
}
</style>
   <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
   <script type="text/javascript">
      google.charts.load('current', {'packages':['gauge']});
      google.charts.setOnLoadCallback(drawChart);
	  google.charts.setOnLoadCallback(drawChart1);
	  google.charts.setOnLoadCallback(drawChart2);
  	  google.charts.setOnLoadCallback(drawChart3);
		function drawChart3() {
		var data3 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['THROTTLE', 100]
        ]);
		var options3 = {max: 100,
		  animation:{duration:10},
          width: 200, height: 200,
		  greenFrom: 0, greenTo: 80,
          redFrom: 90, redTo: 100,
          yellowFrom:80, yellowTo: 90,
          minorTicks: 5
        };
		var chart3 = new google.visualization.Gauge(document.getElementById('chart_div3'));
		chart3.draw(data3, options3);
		setInterval(function() {
		data3.setValue(0, 1, parseInt(showHint('THROT')));
          chart3.draw(data3, options3);
        }, 20);
	}
		function drawChart2() {
		var data2 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['ACCELERATION', 300]
        ]);
		var options2 = {max: 300,
		  animation:{duration:10},
          width: 200, height: 200,
		  greenFrom: 0, greenTo: 250,
          redFrom: 285, redTo: 300,
          yellowFrom:250, yellowTo: 285,
          minorTicks: 5
        };
		var chart2 = new google.visualization.Gauge(document.getElementById('chart_div2'));
		chart2.draw(data2, options2);
		setInterval(function() {
		data2.setValue(0, 1, parseInt(showHint('ACCEL')));
          chart2.draw(data2, options2);
        }, 20);
	}
		//var cc;
		function drawChart1() {
		var data1 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['SPEED', 110]
        ]);
		var options1 = {max: 300,
		  animation:{duration:10},
          width: 200, height: 200,
		  greenFrom: 0, greenTo: 180,
          redFrom: 240, redTo: 300,
          yellowFrom:180, yellowTo: 240,
          minorTicks: 5
        };
		var x = document.getElementById('al_cr1');
		var cc; 
		var chart1 = new google.visualization.Gauge(document.getElementById('chart_div1'));
		chart1.draw(data1, options1);
		setInterval(function() {
			cc= parseInt(showHint('SPEED'));
			
			if (cc > 50) {
				data1.setValue(0, 1, cc);
			    x.classList.toggle("after-box0");
				chart1.draw(data1, options1);
			} else {
				data1.setValue(0, 1, cc);
				//x.classList.toggle("after-box1");
				chart1.draw(data1, options1);
			}

          
        }, 20);
	}
      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['RPM', 110]
        ]);
		
		 var options = {max: 6000,
		  animation:{duration:10},
          width: 200, height: 200,
		  greenFrom: 0, greenTo: 4000,
          redFrom: 4500, redTo: 6000,
          yellowFrom:4000, yellowTo: 4500,
          minorTicks: 5
        };
		
        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
		
        chart.draw(data, options);
		
		setInterval(function() {
		data.setValue(0, 1, parseInt(showHint('RPM')));
          chart.draw(data, options);
        }, 20);
		
	  }
	  
		
function showHint(str) {
	var newurl;
	var textval;
    if (str.length == 0) {
   //     document.getElementById("txtHint").innerHTML = "";
        return;
    } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
				textval = this.responseText;
            }
        };
		newurl = "test_goo1.php?q=" + str;
        xmlhttp.open("GET", newurl, false);
        xmlhttp.send();
		return textval;		
	//	return this.readyState;
    }
}
   </script>

  </head>
  <body>
  <h1>OBD TEST APPLICATION</h1>
 <!-- <p><a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a></p>
 <p><a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a></p>            style="width: 400px; height: 120px;"-->
	<p> <button onclick="window.location.href='https://clda.sqs.com/obd/nn/logout.php'">Logout</button></p>
    <div class="city"  id="chart_div" ></div>
	<div class="city"  id="chart_div1" ></div>
	<div class="city"  id="chart_div2" ></div>
	<div class="city"  id="chart_div3" ></div>
	<div class="after-box" id="al_cr1"  >SPEED LIMIT 50</div>
	<!--<p><a   href="https://www.w3schools.com/html/">Visit our HTML tutorial</a></p>-->
	
  </body>
</html>
