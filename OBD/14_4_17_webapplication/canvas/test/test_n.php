
<!doctype html>
<html>
<!--import RadialGauge from 'C:/xampp/htdocs/OBD/canvas/lib/RadialGauge.js'-->
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
<!--<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://raw.github.com/Mikhus/canv-gauge/master/gauge.min.js"></script>-->
	 <script type="text/javascript">

 var gauge = new RadialGauge({
    renderTo: 'chart_div', // identifier of HTML canvas element or element itself
    //renderTo: 'myCanvas',
	width: 400,
    height: 400,
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
    colorNeedleStart: 'rgba(240, 128, 128, 1)',
    colorNeedleEnd: 'rgba(255, 160, 122, .9)',
    valueBox: true,
    animationRule: 'bounce'
});
// draw initially
gauge.draw();
// animate
setInterval(function(){
   gauge.value = Math.random() * -220 + 220;
}, 1000);

</script>
 <body>
  <h1>OBD TEST APPLICATION</h1>
<!--<canvas id= "myCanvas" ></canvas>-->
    <div id="chart_div" style="width: 400px; height: 120px; ></div>
	
	
  </body>
</html>
