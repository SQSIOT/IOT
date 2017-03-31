

<?php
$serverName = "192.168.162.72";
//$serverName = "192.168.160.65";
$connectionInfo = array( "Database"=>"obd", "UID"=>"obd", "PWD"=>"obd");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     echo "Connection established.<br />";
}else{
     echo "Connection could not be established.<br />";
     die( print_r( sqlsrv_errors(), true));
}

 $sqlq ="SELECT * FROM test";
 
 echo $sqlq;

$result = sqlsrv_query($conn,$sqlq);
if($result === false) {
    die( print_r( sqlsrv_errors(), true) );
}
echo $result." Connection.<br />";

if($result != False)
	{
		if($row = sqlsrv_fetch_Array($result))
		{
			echo "Data feching";
		}
	
}
print_r($row);

// Close the connection. 
sqlsrv_close( $conn );

?>