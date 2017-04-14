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
   #button1{
	   float: left;
width: 200px;
height: 40px;
display:inline-block;

}
.c_gauge {
	position: relative;
   float: left;
  //margin: 10px;
 // padding: 20px;
   max-width: 250px;
   height: 200px;
  // border: 1px solid black;
   display: block;
} 
.c_text {
  float: left;
  margin: 10px;
 // padding: 20px;
  font-size: 150%;
  max-width: 250px;
  height: 20px;
  // border: 1px solid black;
   display: inline-block;
} 
.after-br {
	float: left;
	padding: 10px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 250px;
  height: 80px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 200%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 3%;
border: 6px solid black;  
}
.after-br1 {
	float: left;
	padding: 10px;
	background-color: red;
    clear: left;
    border: 3px solid red;   
  max-width: 250px;
  height: 80px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 200%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 3%;
border: 6px solid black;  
}
.after-box {
	float: left;
	padding: 10px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 250px;
  height: 100px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 400%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 3%;
border: 6px solid black;  
}
.after-box0 {
	float: left;
	padding: 10px;
	background-color: red;
    clear: left;
    border: 3px solid red;   
	height: 100px;
  width: 250px;
  border-radius: 50%;
  text-align: center;
  color: red;
  text-shadow: 3px 2px yellow;
  vertical-align: middle;
  font-size: 400%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 3%;	
  border: 6px solid black;  
}  
.after-box1 {
	float: left;
	padding: 10px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 250px;
  height: 100px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 400%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin: 3%;
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
          ['THROTTLE', 0]
        ]);
		var options3 = {max: 100,
		  animation:{duration:1},
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
          ['ACCELERATION', 0]
        ]);
		var options2 = {max: 300,
		  animation:{duration:1},
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
          ['SPEED', 0]
        ]);
		var options1 = {max: 200,
		  animation:{duration:1},
          width: 200, height: 200,
		  greenFrom: 0, greenTo: 120,
          redFrom: 100, redTo: 200,
          yellowFrom:80, yellowTo: 100,
          minorTicks: 5
        };
		var x = document.getElementById('al_cr1');
		var cc; 
		var cc2;
		var chart1 = new google.visualization.Gauge(document.getElementById('chart_div1'));
		chart1.draw(data1, options1);
		setInterval(function() {
			cc= parseInt(showHint('SPEED'));
			
			if (cc > 50) {
				data1.setValue(0, 1, cc);
			    x.classList.toggle("after-box0");
				chart1.draw(data1, options1);
			} else if(Math.abs(cc-cc2)<30){
				//x.classList.
				chart1.draw(data1, options1);
			}else {
				data1.setValue(0, 1, cc);
				//x.classList.toggle("after-box1");
				chart1.draw(data1, options1);
			}
			cc2= cc;
          
        }, 20);
	}
      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['RPM', 0]
        ]);
		
		 var options = {max: 6000,
		  animation:{duration:0},
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
	<p> <button id ="button1" onclick="window.location.href='https://clda.sqs.com/obd/nn/logout.php'">Logout</button></p>
	<!--<p><button onclick="window.location.href='https://www.w3schools.com'" target="_blank">Location</button></p>-->
	<p><input id ="button1" type="button" value="GPS" onclick="window.open('https://clda.sqs.com/obd/nn/main3.php')" /> </p>
	<script>
	onclick="window.open(this.href,'popUpWindow','height=400,width=600,left=10,top=10,,scrollbars=yes,menubar=no'); return false;"
	</script>
    <div class="c_gauge"  id="chart_div" ></div>
	<div class="c_gauge"  id="chart_div1" ></div>
	

	<div class="c_gauge"  id="chart_div2" ></div>
	<div class="c_gauge"  id="chart_div3" ></div>
	
	<h1 class="c_text"> SPEED LIMIT</h1>
	<div class="after-box" id="al_cr1"  >50</div>
	

	<div class="after-br" id="al_cr2"  >BREAK ALERT</div>
	<!--<p><a   href="https://www.w3schools.com/html/">Visit our HTML tutorial</a></p>-->
	
  </body>
</html>
