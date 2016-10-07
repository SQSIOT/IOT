<?php

ini_set('max_execution_time', 100);
//$serverName = "serverName\sqlexpress"; //serverName\instanceName
//$serverName = "<serverName>";
$connectionInfo = array( "Database"=>"<db>", "UID"=>"<UID>", "PWD"=>"<Password>");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     //echo "Connection established.<br />";
}else{
     echo "Connection could not be established.<br />";
     die( print_r( sqlsrv_errors(), true));
}

$g_sqlq ="select RellayLightMap.LightNumber,loginDetails.UEmpID,loginDetails.ReaderHardWareID, loginDetails.DateTime,loginDetails.type from loginDetails, EMP_REL_MAP,RellayLightMap Where loginDetails.UEmpID = EMP_REL_MAP.UEMPID AND RellayLightMap.RellayID = EMP_REL_MAP.RellayID AND RellayLightMap.Resetcounter = loginDetails.Resetcounter";

//echo $g_sqlq;

$g_result = sqlsrv_query($conn,$g_sqlq);

//Print_r ($g_result);


if($g_result === false) {
    die( print_r( sqlsrv_errors(), true) );
}


$a[] = array();
$i=0;


while( $g_row = sqlsrv_fetch_array($g_result) ) 
	{
	 $a[$i]['LightNumber'] = $g_row['LightNumber'];
	 $a[$i]['UEmpID'] = $g_row['UEmpID'];
	 //Print_r ("<br>".$a[$i]['UEmpID']."</br>"); 
	 $a[$i]['ReaderHardWareID'] = $g_row['ReaderHardWareID'];
	 //Print_r ("<br>".$a[$i]['ReaderHardWareID']."</br>"); 
	 $a[$i]['DateTime'] = $g_row['DateTime'];
	 $a[$i]['type'] =  $g_row['type'];
	 //Print_r ("<br>".$a[$i]['type']."</br>"); 
	 $i++; 
	}

$tot = 0;
$inTime =0;
$outTime =0;
$totn=0;

$R_count = count($a);
//echo $R_count;

$L1H=0;
$L1M=0;
$L1S=0;

$L2H=0;
$L2M=0;
$L2S=0;

$L3H=0;
$L3M=0;
$L3S=0;

$L4H=0;
$L4M=0;
$L4S=0;



If ( $R_count != 1)
{
	//echo "If Loop";
	for ($i=0;$i< count($a);$i++)
		{
			IF ($a[$i]['LightNumber'] == 'Light1')
			{
				//echo "For If Loop light1";
			if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array(108,114,102,116,106,110,104,112))))
				{
					//echo "Light1 If Loop Login";
					$L1Time1 = $a[$i]['DateTime'];
					//print_r ($Time1);
				}
			If($a[$i]['type']=='logout' && ( in_array($a[$i]['ReaderHardWareID'], array(109,115,103,117,107,111,105,113))))
				{
					If(empty($L1Time1))
					{
						//echo "L1 Empty IF loop";
						continue;
					}
					else
					{
					//echo "Light1 If Loop Logout";
					$L1Time2 = $a[$i]['DateTime'];
					$L1dteDiff  = $L1Time1->diff($L1Time2);
					$L1H = $L1H+$L1dteDiff->format("%H");
					$L1M = $L1M+$L1dteDiff->format("%I");
					$L1S = $L1S+$L1dteDiff->format("%S");
					}
				}
			}	
			IF ($a[$i]['LightNumber'] == 'Light2')
			{
				//echo "For If Loop Light2";
			if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array(108,114,102,116,106,110,104,112))))
				{
					//echo "For If Loop login";
					$L2Time1 = $a[$i]['DateTime'];
					//print_r ($Time1);
				}
			If($a[$i]['type']=='logout' && ( in_array($a[$i]['ReaderHardWareID'], array(109,115,103,117,107,111,105,113))))
				{
					If(empty($L2Time1))
					{
						//echo "L3 Empty IF loop";
						continue;
					}
					else
					{
					$L2Time2 = $a[$i]['DateTime'];
					$L2dteDiff  = $L2Time1->diff($L2Time2);
					//Print_r ($L2dteDiff);
					$L2H = $L2H+$L2dteDiff->format("%H");
					//echo $L2H;
					$L2M = $L2M+$L2dteDiff->format("%I");
					$L2S = $L2S+$L2dteDiff->format("%S");
					}
				}
					
			}
			if ($a[$i]['LightNumber'] == 'Light3')
			{
			if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array(108,114,102,116,106,110,104,112))))
				{
					//echo "For If Loop";
					$L3Time1 = $a[$i]['DateTime'];
					//print_r ($Time1);
				}
			If($a[$i]['type']=='logout' && ( in_array($a[$i]['ReaderHardWareID'], array(109,115,103,117,107,111,105,113))))
				{
					If(empty($L3Time1))
					{
						//echo "L3 Empty IF loop";
						continue;
					}
					else
					{
						//echo "L3 NON - Empty IF loop";
						$L3Time2 = $a[$i]['DateTime'];
						$L3dteDiff  = $L3Time1->diff($L3Time2);
						$L3H = $L3H+$L3dteDiff->format("%H");
						$L3M = $L3M+$L3dteDiff->format("%I");
						$L3S = $L3S+$L3dteDiff->format("%S");
					}
				}
					
			}
			if ($a[$i]['LightNumber'] == 'Light4')
			{
			if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array(108,114,102,116,106,110,104,112))))
				{
					//echo "For If Loop";
					$L4Time1 = $a[$i]['DateTime'];
					//print_r ($Time1);
				}
			If($a[$i]['type']=='logout' && ( in_array($a[$i]['ReaderHardWareID'], array(109,115,103,117,107,111,105,113))))
				{
					If(empty($L4Time1))
					{
						//echo "L3 Empty IF loop";
						continue;
					}
					else
					{
					$L4Time2 = $a[$i]['DateTime'];
					$L4dteDiff  = $L4Time1->diff($L4Time2);
					$L4H = $L4H+$L4dteDiff->format("%H");
					$L4M = $L4M+$L4dteDiff->format("%I");
					$L4S = $L4S+$L4dteDiff->format("%S");
					}
				}
			}
		}	
		$L1H = $L1H*3600;
		$L1M = $L1M*60;
		$L1totalTimeON = ($L1H+$L1M+$L1S)/3600;
		If ($L1totalTimeON >= 8000)
		{
			$L1totalTimeOFF = 0;
		}else
		{
			$L1totalTimeOFF = 8000-$L1totalTimeON;
		}

		//echo '<br>'.$L1totalTimeON.'</br>';
		//echo '<br>'.$L1totalTimeOFF.'</br>';
	
		$L2H = $L2H*3600;
		//echo $L2H; 
		$L2M = $L2M*60;
		$L2totalTimeON = ($L2H+$L2M+$L2S)/3600;
		If ($L2totalTimeON >= 8000)
		{
			$L2totalTimeOFF = 0;
		}else
		{
			$L2totalTimeOFF = 8000-$L2totalTimeON;
		}
		//echo '<br>'.$L2totalTimeON.'</br>';
		//echo '<br>'.$L2totalTimeOFF.'</br>';
	
		$L3H = $L3H*3600;
		$L3M = $L3M*60;
		$L3totalTimeON = ($L3H+$L3M+$L3S)/3600;
		
		If ($L3totalTimeON >= 8000)
		{
			$L3totalTimeOFF = 0;
		}else
		{
			$L3totalTimeOFF = 8000-$L3totalTimeON;
		}
				
		//echo '<br>'.$L3totalTimeON.'</br>';
		//echo '<br>'.$L3totalTimeOFF.'</br>';
	
		$L4H = $L4H*3600;
		$L4M = $L4M*60;
		$L4totalTimeON = ($L4H+$L4M+$L4S)/3600;
		If ($L4totalTimeON >= 8000)
		{
			$L4totalTimeOFF = 0;
		}else
		{
			$L4totalTimeOFF = 8000-$L4totalTimeON;
		}
		
		//$L1totalTimeON = 8100;
		//$L1totalTimeOFF = 0;
		
		//$L2totalTimeON = 8100;
		//$L2totalTimeOFF = 0;
		
		//$L3totalTimeON = 8100;
		//$L3totalTimeOFF = 0;
		
		//$L4totalTimeON = 8100;
		//$L4totalTimeOFF = 0;
		
		
		//echo '<br>'.$L4totalTimeON.'</br>';
		//echo '<br>'.$L4totalTimeOFF.'</br>';
		
		If ($L1totalTimeON >= 8000)
		{
			$L1Message = "Light - 1 has completed its life span. Please change light - 1. ";
		}else
		{
			$L1Message = "";
		}
		If ($L2totalTimeON >= 8000)
		{
			$L2Message = "Light - 2 has completed its life span. Please change light - 2. ";
		}else
		{
			$L2Message = "";
		}
		If ($L3totalTimeON >= 8000)
		{
			$L3Message = "Light - 3 has completed its life span. Please change light - 3. ";
		}else
		{
			$L3Message = "";
		}
		If ($L4totalTimeON >= 8000)
		{
			$L4Message = "Light - 4 has completed its life span. Please change the light - 4. ";
		}else
		{
			$L4Message = "";
		}
		
		}
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Light Consumption</title>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart1);
	       
	  function drawChart1() {
			
        var data1 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
		  ['Non Consumtion( in hours )', <?=$L1totalTimeOFF?>],
          ['Consumtion( in hours )',  <?=$L1totalTimeON?>],
          ]);
		
		var options1 = {
          title: 'Light - 1'
        };
		
		 var chart1 = new google.visualization.PieChart(document.getElementById('piechart1'));
         chart1.draw(data1, options1);
	  }  
	  
	  
      google.charts.setOnLoadCallback(drawChart2);
	       
	  function drawChart2() {
			
        var data2 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
		  ['Non Consumtion( in hours )', <?=$L2totalTimeOFF?>],
          ['Consumtion( in hours )',  <?=$L2totalTimeON?>],
          ]);
		
		var options2 = {
          title: 'Light - 2'
        };
		
		 var chart2 = new google.visualization.PieChart(document.getElementById('piechart2'));
        chart2.draw(data2, options2);
	  } 
	  
	  
      google.charts.setOnLoadCallback(drawChart3);
	       
	  function drawChart3() {
			
        var data3 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
		  ['Non Consumtion( in hours )', <?=$L3totalTimeOFF?>],
          ['Consumtion( in hours )',  <?=$L3totalTimeON?>],
          ]);
		
		var options3 = {
          title: 'Light - 3'
        };
		
		 var chart3 = new google.visualization.PieChart(document.getElementById('piechart3'));
        chart3.draw(data3, options3);
	  } 
	  
      google.charts.setOnLoadCallback(drawChart4);
	       
	  function drawChart4() {
			
        var data4 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
		  ['Non Consumtion( in hours )', <?=$L4totalTimeOFF?>],
          ['Consumtion( in hours )',  <?=$L4totalTimeON?>],
          ]);
		
		var options4 = {
          title: 'Light - 4'
        };
		
		 var chart4 = new google.visualization.PieChart(document.getElementById('piechart4'));
        chart4.draw(data4, options4);
	  } 	  
</script>
<script type="text/javascript" language="javascript">
 window.onload=blinkOn;
 	function blinkOn()
	{
	  document.getElementById("blink1").style.color="#000"
	  document.getElementById("blink2").style.color="#000"
	  document.getElementById("blink3").style.color="#000"
	  document.getElementById("blink4").style.color="#000"
	  setTimeout("blinkOff()",1000)
	}
	 
	function blinkOff()
	{
	  document.getElementById("blink1").style.color=""
	  document.getElementById("blink2").style.color=""
	  document.getElementById("blink3").style.color=""
	  document.getElementById("blink4").style.color=""
	  setTimeout("blinkOn()",1000)
	}
</script>
</head>
<body>
<table width="100%" height="100%" border="1">
  <tr>
    <td height="46" colspan="2"><div align="center" style="font-weight:bold;font-size:25">Light Maintenance Graph</div></td>
  </tr>
  <tr>
    <td width="50%" height="250"><div id="piechart1" style="width:100%; height:100%;"></div></td>
	<td width="50%" height="250"><div id="piechart2" style="width:100%; height:100%;"></div></td>
  </tr>
  <tr>
  	<td><font size="3" color="red"><div id="blink1"><?=$L1Message?></div></font></td>
	<td><font size="3" color="red"><div id="blink2"><?=$L2Message?></div></font></td>
  </tr>
    <tr>
    <td width="50%" height="250"><div id="piechart3" style="width:100%; height:100%;"></div></td>
	<td width="50%" height="250"><div id="piechart4" style="width:100%; height:100%;"></div></td>
  </tr>
  <tr>
  	<td><font size="3" color="red"><div id="blink3"><?=$L3Message?></div></font></td>
	<td><font size="3" color="red"><div id="blink4"><?=$L4Message?></div></font></td>
  </tr>
</table>
</body>
</html>