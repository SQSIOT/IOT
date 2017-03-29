<?php
$g_link= mysqli_connect('192.168.162.72','obd','obd');
mysqli_select_db($g_link,'obd');
$query = 'SELECT * FROM para WHERE ID = ( SELECT MAX(ID) FROM para ) ;';//'SELECT * FROM PARA';
global $result;
$result = mysqli_query($g_link,$query);
if (!$result) {
    die('Query failed: ' . mysql_error());
}

global $row;
$allRows = array();
while($row = mysqli_fetch_array($result))
	 {
		 $allRows[] = $row;
	}
global $len;
$len=sizeof($allRows);
$getval = $_GET['q'];
//print_r($allRows['0'][$getval]);
echo $allRows['0'][$getval];
mysqli_close($g_link);
?>