<?php

$link=mysql_connect("192.168.162.72","obd","obd");
mysql_select_db("hauto") or die("Error:" . mysql_error());

if($link === false){
	die("Error: Could not Connect. " . mysqli.connect_error());
}

if(isset($_GET['value']))
{
	$value=$_GET['value'];
	echo "<h2>You have Chosen the button status as:" .$value."</h2>";
	$sql ="INSERT INTO `test` (`ID`, `state`) VALUES (NULL, '$value')";
}

if(mysql_query($sql)){
	echo "Record success.";
}else{	
	echo"Error: could not". mysql_error($link);
}

?>