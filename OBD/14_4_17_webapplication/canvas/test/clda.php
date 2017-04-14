<!doctype html>
<html>

<head>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Gauge Test</title>
    <script src="../gauge.min.js"></script>
    <style>
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
body {
    background-image: url("one.png");
    background-repeat: no-repeat;
    background-position: right top;
    margin-right: 200px;
}
	
	</style>
	
</head>
<body style="width:100%;height:100%">
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://raw.github.com/Mikhus/canv-gauge/master/gauge.min.js"></script>

<!-- customized gauge -->
<!--<canvas data-type="RadialGauge" id="myCanvas"></canvas>-->
<canvas id= "myCanvas" data-type="radial-gauge"
        data-width="400"
        data-glow="true"
        data-height="250"
        data-units="km/h"
        data-title="SPEED"
		data-value="0"
        data-min-value="0"
        data-max-value="220"
        data-major-ticks="0,20,40,60,80,100,120,140,160,180,200,220"
        data-minor-ticks="2"
        data-stroke-ticks="false"
        data-highlights='[
            { "from": 0, "to": 70, "color": "#47ad47" },
            { "from": 70, "to": 120, "color": "#ff0" },
            { "from": 120, "to": 180, "color": "#F00" },
            { "from": 180, "to": 220, "color": "#000073" },
            { "from": 200, "to": 220, "color": "rgba(0,0,255,.25)" }	
        ]'
        data-color-plate="#222"
        data-color-major-ticks="#f5f5f5"
        data-color-minor-ticks="#ddd"
        data-color-title="#00ffff"
        data-color-units="#00ffff"
        data-color-numbers="#eee"
		data-visibility="4"
        data-color-needle-start="rgba(240, 128, 128, 1)"
        data-color-needle-end="rgba(255, 160, 122, .9)"
        data-value-box="true"
        data-animation-rule="bounce"
        data-animation-duration="5"
        data-needle-shadow="false"
></canvas>

<canvas data-type="radial-gauge"
        data-width="400"
        data-glow="false"
        data-height="250"
        data-units=""
        data-title="RPM 
		1*1000"
        data-value="22"
        data-min-value="0"
        data-max-value="6"
        data-major-ticks="0,1,2,3,4,5,6"
        data-minor-ticks="0.5"
        data-stroke-ticks="false"
        data-highlights='[
            { "from": 0, "to": 2, "color": "#47ad47" },
            { "from": 2, "to": 4, "color": "#ff0" },
            { "from": 4, "to": 5, "color": "#F00" },
            { "from": 5, "to": 6, "color": "#000073" },
            { "from": 6, "to": 0, "color": "#0000" }
        ]'
        data-color-plate="#222"
        data-color-major-ticks="#f5f5f5"
        data-color-minor-ticks="#ddd"
        data-color-title="#00ffff "
        data-color-units="#00ffff"
        data-color-numbers="#eee"
        data-color-needle-start="rgba(240, 128, 128, 1)"
        data-color-needle-end="rgba(255, 160, 122, .9)"
        data-value-box="true"
        data-animation-rule="bounce"
        data-animation-duration="500"
        data-needle-shadow="false"
></canvas>
<br></br>
<br></br>
<br></br>
<div class="circle">
 <div class="circle__content">50
 <div class="body"></div>
 </div>
</div>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>

<canvas data-type="radial-gauge"
        data-width="400"
        data-glow="false"
        data-height="250"
        data-units="%"
        data-title="THROTTLE"
        data-value="22"
        data-min-value="0"
        data-max-value="100"
        data-major-ticks="0,10,20,30,40,50,60,70,80,90,100"
        data-minor-ticks="10"
        data-stroke-ticks="false"
        data-highlights='[
            { "from": 0, "to": 30, "color": "#47ad47" },
            { "from": 30, "to": 60, "color": "#ff0" },
            { "from": 60, "to": 80, "color": "#F00" },
            { "from": 80, "to": 100, "color": "#000073" },
            { "from": 100, "to": 0, "color": "#0000" }
        ]'
        data-color-plate="#222"
        data-color-major-ticks="#f5f5f5"
        data-color-minor-ticks="#ddd"
        data-color-title="#00ffff "
        data-color-units="#00ffff"
		data-visibility="4"
        data-color-numbers="#eee"
        data-color-needle-start="rgba(240, 128, 128, 1)"
        data-color-needle-end="rgba(255, 160, 122, .9)"
        data-value-box="true"
        data-animation-rule="bounce"
        data-animation-duration="500"
        data-needle-shadow="false"
></canvas>

<canvas data-type="radial-gauge"
        data-width="400"
        data-glow="false"
        data-height="250"
        data-units="mps"
        data-title="ACCELERATION 1*10"
        data-value="23"
        data-min-value="0"
        data-max-value="300"
        data-major-ticks="0,50,100,150,200,250,300"
        data-minor-ticks="5"
        data-stroke-ticks="false"
        data-highlights='[
			{ "from": 0, "to": 100, "color": "#47ad47" },
            { "from": 100, "to": 150, "color": "#ff0" },
            { "from": 150, "to": 220, "color": "#F00" },
            { "from": 220, "to": 300, "color": "#000073" },
            { "from": 300, "to": 0, "color": "#0000" }
            
        ]'
        data-color-plate="#222"
        data-color-major-ticks="#f5f5f5"
        data-color-minor-ticks="#ddd"
        data-color-title="#00ffff "
        data-color-units="#00ffff"
		data-visibility="4"
        data-color-numbers="#eee"
        data-color-needle-start="rgba(240, 128, 128, 1)"
        data-color-needle-end="rgba(255, 160, 122, .9)"
        data-value-box="true"
        data-animation-rule="bounce"
        data-animation-duration="500"
        data-needle-shadow="false"
></canvas>

<!-- default gauge <canvas data-type="radial-gauge" data-width="200" data-height="200"></canvas> -->

</body>
	 <script type="text/javascript">
	 if (!Array.prototype.forEach) {
    Array.prototype.forEach = function(cb) {
        var i = 0, s = this.length;
        for (; i < s; i++) {
            cb && cb(this[i], i, this);
        }
    }
}

document.fonts && document.fonts.forEach(function(font) {
    font.loaded.then(function() {
        if (font.family.match(/Led/)) {
            document.gauges.forEach(function(gauge) {
                gauge.update();
                gauge.options.renderTo.style.visibility = 'visible';
            });
        }
    });
});
function animateGauges() {
    document.gauges.forEach(function(gauge) {
        timers.push(setInterval(function() {
            gauge.value = Math.random() *
                (gauge.options.maxValue - gauge.options.minValue) +
                gauge.options.minValue;
        }, gauge.animation.duration + 50));
    });
}
	var gauge = document.gauges.get('myCanvas');
	//var gauge = new radial-gauge({ renderTo:'myCanvas'});
	//var c=document.getElementById("myCanvas");
	 setInterval(function() {
		 gauge.value= 100; 
		 //console.log(12);
		 //console.log(gauge1.value);
		 //gauge1.value = 12;//Math.random() *
                //(gauge.options.maxValue - gauge.options.minValue) +
                //gauge.options.minValue;
	 }, 10);

	// initialize gauge with value on construction
//var gauge = new LinearGauge({ renderTo: 'myCanvas', value: 50 });
/*var radial = new radial-gauge({
    renderTo: 'myCanva',
    width: 200,
    height: 200,
    units: 'Km/h',
    title: false,
    value: 0,
    minValue: 0,
    maxValue: 220,
    majorTicks: [
        '0','20','40','60','80','100','120','140','160','180','200','220'
    ],
    minorTicks: 2,
    strokeTicks: false,
    highlights: [
        { from: 0, to: 50, color: 'rgba(0,255,0,.15)' },
        { from: 50, to: 100, color: 'rgba(255,255,0,.15)' },
        { from: 100, to: 150, color: 'rgba(255,30,0,.25)' },
        { from: 150, to: 200, color: 'rgba(255,0,225,.25)' },
        { from: 200, to: 220, color: 'rgba(0,0,255,.25)' }
    ],
    colorPlate: '#222',
    colorMajorTicks: '#f5f5f5',
    colorMinorTicks: '#ddd',
    colorTitle: '#fff',
    colorUnits: '#ccc',
    colorNumbers: '#eee',
    colorNeedle: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce',
    animationDuration: 500
});*/
//radial.draw();

//var gauge = document.gauges.get('myCanvas');
//console.log(gauge.value);
///////////////////////////////////////////////////////////////////////
//var gauge = new RadialGauge({ renderTo: 'myCanvas', value: 50 });
				
// change the value at runtime
//gauge.value = 33.2;	
//////////////////////////////////////////////////////////////////////	 		
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
