<?php
session_start();
if(empty($_SESSION['login_user']))
{
	header("Location: index.php");
}
?>
<!doctype html>
<html>

<head>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Gauge Test</title>
    <script src="../gauge.min.js"></script>
    <style>
	   h1 {
	   //border-bottom: 8px solid #57c4d0;
	   //border-bottom: 1px #d2202f solid;
    color: black//rgb(146, 179, 132);
	  padding-bottom: 5px;
  position: relative;
  //margin-left: 30%
}
h1:before{
    content: "";
    position: absolute;
    width: 50%;
    height: 1px;
    bottom: 0;
    left: -2%;
    border-bottom: 1px solid red;
}
   #button1{
	float: left;
width: 200px;
height: 40px;
display:inline-block;
margin-top: 6%;

}
	.circle {
  position: absolute;
  margin-top:10px;
  margin-left:300px;
  padding:10px;
  display: inline-block;
  background-color:red;
  background-image: url("one.png");
  color:#f00f;
  text-align: center;
  border-radius: 50%;
 outline-style: solid
 outline-color: green;
  
}
.c_text {
  float: left;
  margin-top: -3%;
  margin-left: 43%;//20px;
 // padding:20px;
  font-size: 180%;
  max-width: 200px;
  height: 1px;
  color: black;
     vertical-align: middle;
   //border: 1px solid black;
   display: inline-block;
} 

.c_gauge {
	position: relative;
   float: left;
  //margin: 6px;
  //margin-top: 10%;
  //margin-left: 10%;
  padding: 8px;
   //max-width: 250px;
   //height: 200px;
   //border: 1px solid black;
   //display: inline-block;
} 
.circle__content {
  display: table-cell;
  padding: 1em;
  vertical-align: middle;
  font-size:4em;
 font-weight:bold;
 text-shadow: 4px 2px yellow;
  border-radius: 55%;
 border-style:solid;
 outline-style: solid
 outline-color: green;

}
.after-box {
	float: left;
	padding: 2px;
	background-color: green;
    clear: left;
    border: 3px solid green;   
  max-width: 150px;
  height: 100px;
  border-radius: 50%;
  text-align: center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 500%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin-left: 46%;
  margin-top: 1%;
border: 6px solid black;  
}
.after-box0 {
	float: left;
	padding: 2px;
	background-color: red;
    clear: left;
    border: 3px solid red;   
  max-width: 150px;
  height: 100px;
  border-radius: 50%;
  text-align: center;
  color: red;
  text-shadow: 3px 2px yellow;
  vertical-align: middle;
  font-size: 500%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin-left: 46%;
  margin-top: 1%;
  border: 6px solid black;  
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
  //text-align:  center;
  color: yellow;
  text-shadow: 3px 2px red;
  vertical-align: middle;
  font-size: 230%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin-left: 39%;
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
  //text-align:  center;
  color: red;
  text-shadow: 3px 2px yellow;
  vertical-align: middle;
  font-size: 230%;
  position: relative;
  //box-shadow: inset -10px -10px 100px #000, 10px 10px 20px black, inset 0px 0px 10px black;
  display: inline;
  margin-left: 39%;
border: 6px solid black;  
}
body {
    background-image: url("road1.jpg");
    //background-repeat: no-repeat;
    //background-position: right top;
    //margin-right: 200px;
	  background-size: cover;
}
	
	</style>
</head>
<body >
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://raw.github.com/Mikhus/canv-gauge/master/gauge.min.js"></script>
  <h1 style= "margin-left: 34%">OBD TEST APPLICATION</h1>
  	<p> <button id ="button1" onclick="window.location.href='https://clda.sqs.com/obd/canvas/test/logout.php'" style= "float: right">Logout</button></p>
	<!--<p><button onclick="window.location.href='https://www.w3schools.com'" target="_blank">Location</button></p>-->
	<p><input id ="button1" type="button" value="GPS" onclick="window.open('https://clda.sqs.com/obd/nn/main3.php')" /> </p>
	<script>
	onclick="window.open(this.href,'popUpWindow','height=400,width=600,left=10,top=10,,scrollbars=yes,menubar=no'); return false;"
	</script>
<canvas class="c_gauge"   style= "margin-top: -1%; margin-left: 9%;" data-type="RadialGauge" id="g1"></canvas>
<canvas class="c_gauge" style= "margin-top: -1%; margin-left: 7%;" data-type="RadialGauge" id="g2"></canvas>

	<div class="c_text"> SPEED LIMIT</div>
	<div class="after-box" id="al_cr1"  >50</div>
	<!--<div class="after-br" id="al_cr2"  >BRAKE ALERT</div>-->
	
<canvas class="c_gauge" style= "margin-top: -1%; margin-left: 25%;" data-type="RadialGauge" id="g3"></canvas>
<canvas class="c_gauge" style= "margin-top: -1%; margin-left: 8%;" data-type="RadialGauge" id="g4"></canvas>
	
</body>
<script type="text/javascript">
 var gauge = new RadialGauge({
    renderTo: 'g1', // identifier of HTML canvas element or element itself
    width: 250,
    height: 250,
    units: 'Km/h',
    title: 'SPEED',
    value: 0,
    minValue: 0,
    maxValue: 220,
    majorTicks: [
        '0','20','40','60','80','100','120','140','160','180','200','220'
    ],
    minorTicks: 2,
    strokeTicks: false,
    highlights: [
        { from: 0, to: 120, color: "#47ad47" },//'rgba(0,255,0,.15)' },
        { from: 120, to: 170, color: '#ff0'},//'rgba(255,255,0,.15)' },
        { from: 170, to: 220, color: "#F00" }//'rgba(255,30,0,.25)' },
        //{ from: 180, to: 200, color: 'rgba(255,0,225,.25)' },
        //{ from: 200, to: 220, color: 'rgba(0,0,255,.25)' }
    ],
    colorPlate: '#222',
    colorMajorTicks: '#f5f5f5',
    colorMinorTicks: '#ddd',
    colorTitle: '#fff',
    colorUnits: '#ccc',
    colorNumbers: '#eee',
    colorNeedleStart: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce'
});
// draw initially
gauge.draw();
var cc; 
var cc2;
var x = document.getElementById('al_cr1');
var y = document.getElementById('a1_cr2');
var c= 1; 
// animate
setInterval(() => {
	cc= showHint('SPEED');
	//Math.abs(cc2-cc)
	cc3= cc2-cc;
	if (cc > 50) {
				
			    x.classList.toggle("after-box0");
				//if (c > 1){y.classList.toggle("after-br1");c= c-1;}
				//if (c < 1){y.className = "after-br";}
	}else if (cc < 50 ) {
				
				x.className = "after-box";
				//if (c > 1){y.classList.toggle("after-br1");c= c-1;}
				//if (c < 1){y.className = "after-br";}
	} //else if(cc3 >30){

		//		y.className= "after-br1";
			//	c= 5;
	//}			
	//else {
					
		//	y.className = "after-br";

	//}
	cc2= cc;
   gauge.value = cc;//Math.random() * -220 + 220;
}, 200);

var gauge2 = new RadialGauge({
    renderTo: 'g2', // identifier of HTML canvas element or element itself
    width: 250,
    height: 250,
    //units: '',
    title: 'RPM x1000',
    value: 0,
    minValue: 0,
    maxValue: 6,
    majorTicks: [
        '0','1','2','3','4','5','6'
    ],
    minorTicks: 2,
    strokeTicks: false,
    highlights: [
        { from: 0, to: 3, color: "#47ad47" },//'rgba(0,255,0,.15)' },
        { from: 3, to: 4, color: '#ff0'},//'rgba(255,255,0,.15)' },
        { from: 4, to: 6, color: "#F00" }//'rgba(255,30,0,.25)' },
        //{ from: 180, to: 200, color: 'rgba(255,0,225,.25)' },
        //{ from: 200, to: 220, color: 'rgba(0,0,255,.25)' }
    ],
    colorPlate: '#222',
    colorMajorTicks: '#f5f5f5',
    colorMinorTicks: '#ddd',
    colorTitle: '#fff',
    colorUnits: '#ccc',
    colorNumbers: '#eee',
    colorNeedleStart: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce'
});
gauge2.draw();
// animate

setInterval(() => {
   gauge2.value = (showHint('RPM'))/1000;//Math.random() * -6 + 6;
}, 200);

var gauge3 = new RadialGauge({
    renderTo: 'g3', // identifier of HTML canvas element or element itself
    width: 250,
    height: 250,
    units: '%',
    title: 'THROTTLE',
    value: 0,
    minValue: 0,
    maxValue: 100,
    majorTicks: [
        '0','10','20','30','40','50','60','70','80','90','100'
    ],
    minorTicks: 2,
    strokeTicks: false,
    highlights: [
	    { from: 0, to: 10, color: '#ff0'},//'rgba(255,255,0,.15)' },
        { from: 10, to: 80, color: "#47ad47" },//'rgba(0,255,0,.15)' },
    
        { from: 80, to: 100, color: "#F00" }//'rgba(255,30,0,.25)' }
        //{ from: 180, to: 200, color: 'rgba(255,0,225,.25)' },
        //{ from: 200, to: 220, color: 'rgba(0,0,255,.25)' }
    ],
    colorPlate: '#222',
    colorMajorTicks: '#f5f5f5',
    colorMinorTicks: '#ddd',
    colorTitle: '#fff',
    colorUnits: '#ccc',
    colorNumbers: '#eee',
    colorNeedleStart: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce'
});
gauge3.draw();
// animate
setInterval(() => {
   gauge3.value = showHint('THROT');//Math.random() * -6 + 6;
}, 200);

var gauge4 = new RadialGauge({
    renderTo: 'g4', // identifier of HTML canvas element or element itself
    width: 250,
    height: 250,
    units: 'm/s^2',
    title: 'ACCELERATION',
    value: 0,
    minValue: 0,
    maxValue: 400,
    majorTicks: [
        '0','40','80','120','160','200','240','280','320','360','400'
    ],
    minorTicks: 2,
    strokeTicks: false,
    highlights: [
        //{ from: 0, to: 3, color: 'rgba(0,255,0,.15)' },
        { from: 0, to: 400, color: "#47ad47" },//'rgba(255,255,0,.15)' }
        //{ from: 4, to: 6, color: 'rgba(255,30,0,.25)' },
        //{ from: 180, to: 200, color: 'rgba(255,0,225,.25)' },
        //{ from: 200, to: 220, color: 'rgba(0,0,255,.25)' }
    ],
    colorPlate: '#222',
    colorMajorTicks: '#f5f5f5',
    colorMinorTicks: '#ddd',
    colorTitle: '#fff',
    colorUnits: '#ccc',
    colorNumbers: '#eee',
    colorNeedleStart: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce'
});
gauge4.draw();
// animate
setInterval(() => {
   gauge4.value = showHint('ACCEL');//Math.random() * -6 + 6;
}, 200);
//////////////////////////////////////////////////
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
</html>