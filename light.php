<?php

ini_set('max_execution_time', 100);
//$serverName = "serverName\sqlexpress"; //serverName\instanceName
$serverName = "VIRTUALADMIN-PC";
//$serverName = "192.168.1.5";
$connectionInfo = array( "Database"=>"IoT", "UID"=>"sa", "PWD"=>"Password123");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     //echo "Connection established.<br />";
}else{
     echo "Connection could not be established.<br />";
     die( print_r( sqlsrv_errors(), true));
}

$sqlq ="select DISTINCT LightNumber from dbo.RellayLightMap";
$result = sqlsrv_query($conn,$sqlq);

Function GetOptions($result1)
{
if($result1 != False)
	{
		$SQLData = array(); 

		while ($row = sqlsrv_fetch_Array($result1))
		{
			$SQLData[] = $row;
		}
	}


echo "<select name='LID'><option value=''>Select One</option>";
For ($i=0; $i<=(count($SQLData)-1); $i++)
	{
		$ID = $SQLData[$i]['0'];
		
		echo "<option value='$ID'>$ID</option>";

	}
echo "</select>";
}


$Q_LID = "Please Select the parameter and generate Report.";
$totalTimeON = 0;


if(isset($_POST['submit']))
{
$Q_LID = $_POST['LID'];  // Storing Selected Value In Variable
$Q_FromDate = $_POST['FromDate'];  // Storing Selected Value In Variable
$Q_ToDate = $_POST['ToDate'];  // Storing Selected Value In Variable

//echo $Q_LID;

$g_sqlq ="select RellayLightMap.LightNumber,loginDetails.UEmpID,loginDetails.ReaderHardWareID, loginDetails.DateTime,loginDetails.type from loginDetails, EMP_REL_MAP,RellayLightMap Where loginDetails.UEmpID = EMP_REL_MAP.UEMPID AND RellayLightMap.RellayID = EMP_REL_MAP.RellayID AND RellayLightMap.LightNumber = '$Q_LID' and Convert (date,DateTime,120) between '$Q_FromDate' AND '$Q_ToDate'";

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

$H=0;
$M=0;
$S=0;

If ( $R_count != 1)
	{
	//echo "If Loop";
	for ($i=0;$i< count($a);$i++)
		{
			if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array(108,114,102,116,106,110,104,112))))
				{
					//echo "For If Loop";
					$Time1 = $a[$i]['DateTime'];
					//print_r ($Time1);
				}
			If($a[$i]['type']=='logout' && ( in_array($a[$i]['ReaderHardWareID'], array(109,115,103,117,107,111,105,113))))
				{
					If(empty($Time1))
					{
						//echo "Empty IF loop";
						continue;
					}
					else
					{
					$Time2 = $a[$i]['DateTime'];
					$dteDiff  = $Time1->diff($Time2);
					$H = $H+$dteDiff->format("%H");
					$M = $M+$dteDiff->format("%I");
					$S = $S+$dteDiff->format("%S");
					}
				}
					
					//print_r ($Time2);
					
					//Print_r ("<br>".$H."</br>");
					//Print_r ("<br>".$M."</br>");
					//Print_r ("<br>".$S."</br>");
		}

		$datetime1 = new DateTime($Q_FromDate);
		$datetime2 = new DateTime($Q_ToDate);
		$interval = $datetime1->diff($datetime2);
		$Days = $interval->format('%a');
		//echo $Days;

		
		
		$H = $H*3600;
		$M = $M*60;
		$totalTimeON = ($H+$M+$S)/3600;
		//echo $totalTimeON;
		If ($Days != '0')
		{$totalTimeOFF = ($Days*24)-$totalTimeON;}
		else
		{$totalTimeOFF = 24-$totalTimeON;}
		//echo $totalTimeOFF;

		
	}	
	else
	{
	echo "No Data fount.";
	$totalTimeON = "No Data found";
	}
}
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Untitled Document</title>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
	       
	  function drawChart() {
			
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
		  ['Non Consumtion( in hours )', <?=$totalTimeOFF?>],
          ['Consumtion( in hours )',  <?=$totalTimeON?>],
          ]);
		
		var options = {
          title: 'Daily Consumption of Electricity'
        };
		
		 var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
	  } 
	 
	  
</script>
</head>
<form action="#" method="post">
<body>
<table width="100%" height="100%" border="1">
  <tr>
    <td height="46" colspan="2"><div align="center">Electricity Consumption </div></td>
  </tr>
    <tr>
	<td><?php GetOptions($result); ?>
		<input type="date" id="FromDate" name="FromDate">
		<input type="date" id="ToDate" name="ToDate">
		<input type="submit" name="submit" value="Generate Report" /></td>
  </tr>
  <tr>
    <td width="50%" height="98%"><div id="piechart" style="width:100%; height:100%;"></div>
</td>
	<td width="50%">
	  <table width="100%" height="10" border="1" >
	    <tr  height="2">
		  <td> LightNumber</td>
		  <td> Consumtion (hours)</td>
		</tr>
		<tr  height="2">
		  <td><?=$Q_LID?></td>
		  <td><?=$totalTimeON?></td>
		</tr>
	  </table>
	</td>
	
  </tr>
  <tr>
    <td colspan="2" height="2%">&nbsp;</td>
  </tr>
</table>
</body>
</form>
</html>