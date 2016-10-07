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
$Q_TimePeriod = $_POST['TimePeriod'];  // Storing Selected Value In Variable
$Q_DateOption = $_POST['DateOption'];
//$Q_ToDate = $_POST['ToDate'];  // Storing Selected Value In Variable
//echo $Q_LID;
//echo $Q_TimePeriod;
//echo $Q_FromDate;
//echo $Q_ToDate;
//echo $Q_DateOption;

$g_sqlq ="select EMP_REL_MAP.ReaderHWID,RellayLightMap.LightNumber,loginDetails.UEmpID,loginDetails.ReaderHardWareID, loginDetails.DateTime,loginDetails.type from loginDetails, EMP_REL_MAP,RellayLightMap Where loginDetails.UEmpID = EMP_REL_MAP.UEMPID AND RellayLightMap.RellayID = EMP_REL_MAP.RellayID AND RellayLightMap.LightNumber = '$Q_LID'";

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
	 $a[$i]['EmpHWID'] = $g_row['ReaderHWID'];
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
			$EMPHWIDIN = $a[$i]['EmpHWID'];
			$EMPHWIDOUT = $EMPHWIDIN - 1;
			
			if ($Q_DateOption == 'DD')
			{		
				//Print_r($EMPHWIDIN);
				//Print_r($EMPHWIDOUT);
				
				If ($Q_TimePeriod == 'Daily')
				{
					//echo "Daily";
					$TimePeriodIN = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDIN,108,114,102,116,106,110,104,112))) && date_format($a[$i]['DateTime'],"d") == date("d") && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));	
					$TimePeriodOUT = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDOUT,109,115,103,117,107,111,105,113))) && date_format($a[$i]['DateTime'],"d") == date("d") && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));	
					//echo date_format($a[$i]['DateTime'],"d");
					//echo date("d"); 
					$Days = 0;
					
				}
				If ($Q_TimePeriod == 'Weekly')
				{
					//echo "Weekly";
					$TimePeriodIN = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDIN,108,114,102,116,106,110,104,112))) && date_format($a[$i]['DateTime'],"w") <= date("w") && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));
					$TimePeriodOUT = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDOUT,109,115,103,117,107,111,105,113))) && date_format($a[$i]['DateTime'],"w") <= date("w") && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));
					$Days = date("w");
					//echo $Days;					
					
				}
				
				If ($Q_TimePeriod == 'Monthly')
				{
					//echo "Monthly";
					$TimePeriodIN = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDIN,108,114,102,116,106,110,104,112))) && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));
					$TimePeriodOUT = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDOUT,109,115,103,117,107,111,105,113))) && date_format($a[$i]['DateTime'],"m") == date("m") && date_format($a[$i]['DateTime'],"y") == date("y"));
					$Days = date("d");
					//echo date("d");
					
				}			
				If ($Q_TimePeriod == 'Yearly')
				{
					//echo "Yearly";
					$TimePeriodIN = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDIN,108,114,102,116,106,110,104,112))) && date_format($a[$i]['DateTime'],"y") == date("y"));
					$TimePeriodOUT = (( in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDOUT,109,115,103,117,107,111,105,113))) && date_format($a[$i]['DateTime'],"y") == date("y"));
					$datetime1 = new DateTime('2016-01-01');
					$datetime2 = New DateTime (date('Y-m-d'));
					//Print_r ($datetime1);
					//Print_r ($datetime2);
					$interval = $datetime1->diff($datetime2);
					//Print_r ($interval);
					$Days = $interval->format('%a');
					//echo $Days;
				}			
			
			}
			if ($Q_DateOption == 'Date') 
			{
				//echo "Date Loop";
				//Print_r($EMPHWIDIN);
				//Print_r($EMPHWIDOUT);


				$TimePeriodIN = (in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDIN,108,114,102,116,106,110,104,112)) && date_format($a[$i]['DateTime'],"Y-m-d") >= $Q_FromDate && date_format($a[$i]['DateTime'],"Y-m-d") <= $Q_ToDate);
				$TimePeriodOUT = (in_array($a[$i]['ReaderHardWareID'], array($EMPHWIDOUT,109,115,103,117,107,111,105,113)) && date_format($a[$i]['DateTime'],"Y-m-d") >= $Q_FromDate && date_format($a[$i]['DateTime'],"Y-m-d") <= $Q_ToDate);
				$datetime1 = new DateTime($Q_FromDate);
				//Print_r ($datetime1);
				$datetime2 = new DateTime($Q_ToDate);
				//Print_r ($datetime2);
				$interval = $datetime1->diff($datetime2);
				$Days = $interval->format('%a');
				//echo $Days;
			}
			
			
			if ($a[$i]['type']=='login'  && $TimePeriodIN)
				{
					//echo "For If Login";
					$Time1 = $a[$i]['DateTime'];
					//Print_r($Time1);
					//$Temp = $a[$i]['ReaderHardWareID'];
					//Print_r($Temp);

				}
			If($a[$i]['type']=='logout' && $TimePeriodOUT)
				{
					If(empty($Time1))
					{
						//echo "Empty IF Logout";
						continue;
					}
					else
					{
					//echo "IF Logout";
					$Time2 = $a[$i]['DateTime'];
					$dteDiff  = $Time1->diff($Time2);
					//Print_r($Time2);
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


				
		$H = $H*3600;
		$M = $M*60;
		$totalTimeON = ($H+$M+$S)/3600;
		//echo $totalTimeON;
		//echo $Days;
		If ($Days != 01 AND $Days != 0)
		{$totalTimeOFF = ($Days*24)-$totalTimeON;
		 //echo "(Days*24)-totalTimeON";
		}
		else
		{$totalTimeOFF = 24-$totalTimeON;
			//echo "24-totalTimeON";
		}
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
		<input type="radio" name="DateOption" value="DD">Dropdown
		<input type="radio" name="DateOption" value="Date">Date
		<?php echo "<select name='TimePeriod'>
			<option value='Daily'>Daily</option>
			<option value='Weekly'>Weekly</option>
			<option value='Monthly'>Monthly</option>
			<option value='Yearly'>Yearly</option>
			</select>"; ?>
		<input type="date" id="FromDate" name="FromDate">
		<input type="date" id="ToDate" name="ToDate">
		<input type="submit" name="submit" value="Generate Report" />
	</td>
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