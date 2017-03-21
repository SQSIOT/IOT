<?php

$g_link= mysqli_connect("192.168.162.72", "obd", "obd")or die("cannot connect");
mysqli_select_db($g_link,"obd");            
//$sql=("SELECT * FROM `gps`");
$query = 'SELECT * FROM gps WHERE ID = ( SELECT MAX(ID) FROM gps ) ;'; 
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
print_r($allRows['0'][$getval]);
mysqli_close($g_link);

?>
