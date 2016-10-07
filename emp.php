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

$sqlq ="select DISTINCT UEmpID from dbo.loginDetails";
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

echo "<select name='Employee'><option value=''>Select One</option>";
For ($i=0; $i<=(count($SQLData)-1); $i++)
	{
		$ID = $SQLData[$i]['0'];
		
		echo "<option value='$ID'>$ID</option>";

	}
echo "</select>";
}

//$Q_EMP = "";
//$totalTimeON = "";


if(isset($_POST['submit']))
{
$Q_EMP = $_POST['Employee'];  // Storing Selected Value In Variable
$Q_FromDate = $_POST['FromDate'];  // Storing Selected Value In Variable
$Q_ToDate = $_POST['ToDate'];  // Storing Selected Value In Variable

//echo $Q_EMP;

$g_sqlq ="select UEmpID,ReaderHardWareID, DateTime,type from dbo.loginDetails where UEmpID='$Q_EMP' and Convert (date,DateTime,120) between '$Q_FromDate' AND '$Q_ToDate'";
$ReaderHW = "Select TOP 1  Count (ReaderHardWareID)as ID, ReaderHardWareID from logindetails where UEmpID = '$Q_EMP' and Type = 'login' and Convert (date,DateTime,120) between '$Q_FromDate' AND '$Q_ToDate'  group by ReaderHardWareID order by ID desc";

echo $ReaderHW;
echo $g_sqlq;

$g_result = sqlsrv_query($conn,$g_sqlq);
$RHW_result = sqlsrv_query($conn,$ReaderHW);

//Print_r ($g_result);
//Print_r ($RHW_result);

if($g_result === false) {
    die( print_r( sqlsrv_errors(), true) );
}

if($RHW_result === false) {
    die( print_r( sqlsrv_errors(), true) );
}

$a[] = array();
$b[] = array();
$i=0;
$j=0;

while( $g_row = sqlsrv_fetch_array($g_result) ) {

	 $a[$i]['UEmpID'] = $g_row['UEmpID'];
	 $a[$i]['ReaderHardWareID'] = $g_row['ReaderHardWareID'];
	 $a[$i]['tmpdate'] =  date_format($g_row['DateTime'],"Y/m/d");
	 $a[$i]['tmptime'] =  date_format($g_row['DateTime'],"H:i:s");
	 $a[$i]['DateTime'] = $g_row['DateTime'];
	 $a[$i]['type'] =  $g_row['type'];
	 $i++; 
}

while( $RHW_row = sqlsrv_fetch_array($RHW_result) ) {

	 $b[$j]['RHWID'] = $RHW_row['ReaderHardWareID'];
	 $RHWID1 = $b[$j]['RHWID'];
	 //echo $RHWID1;
	 $j++; 
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
		//echo "For Loop";

	if ($a[$i]['type']=='login' && ( in_array($a[$i]['ReaderHardWareID'], array($RHWID1,108,114,102,116,106,110,104,112))))
	{
			//echo "For If Loop";
		
		$Time1 = $a[$i]['DateTime'];
		//$Diffdate1  = $Time1->format("y-m-d");
		//print_r ($Time1);
		//print_r ('<br>'.$Diffdate1.'</br>');
		$Time2 = $a[$i+1]['DateTime'];
		//$Diffdate2  = $Time2->format("y-m-d");
		//print_r ($Time2);
		//print_r ('<br>'.$Diffdate2.'</br>');
		$dteDiff  = $Time1->diff($Time2);
		$H = $H+$dteDiff->format("%H");
		$M = $M+$dteDiff->format("%I");
		$S = $S+$dteDiff->format("%S");
		//Print_r ("<br>".$H."</br>");
		//Print_r ("<br>".$M."</br>");
		//Print_r ("<br>".$S."</br>");
		
	}

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
	echo "No Data fount. Employee may be absent on this day.";
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
		  <td> EmpID</td>
		  <td> Consumtion (hours)</td>
		</tr>
		<tr  height="2">
		  <td><?=$Q_EMP?></td>
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