<?php
ini_set('max_execution_time', 100);
//$serverName = "serverName\sqlexpress"; //serverName\instanceName
//$serverName = "<serverName>";
$connectionInfo = array( "Database"=>"<db>", "UID"=>"<UID>", "PWD"=>"<Password>");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

if( $conn ) {
     echo "Connection established.<br />";
}else{
     echo "Connection could not be established.<br />";
     die( print_r( sqlsrv_errors(), true));
}

 $sqlq ="select UEmpID,ReaderHardWareID,Type from IoTDB";

$result = sqlsrv_query($conn,$sqlq);

if($result === false) {
    die( print_r( sqlsrv_errors(), true) );
}
echo $result." Connection.<br />";

if($result != False)
	{
		$SQLData = array(); 

		while ($row = sqlsrv_fetch_Array($result))
		{
			$SQLData[] = $row;
		}
	}

For ($i=0; $i<=(count($SQLData)-1); $i++)
	{
		// create a new cURL resource
		$ch = curl_init();
		$IP = 'http://192.168.163.150/';

		$URL = $IP.$SQLData[$i]['0'].$SQLData[$i]['1'].$SQLData[$i]['2'];
		
		// set URL and other appropriate options
		curl_setopt($ch, CURLOPT_URL, $URL);
		curl_setopt($ch, CURLOPT_HEADER, 0);

		// grab URL and pass it to the browser
		curl_exec($ch);
		
		// close cURL resource, and free up system resources
		curl_close($ch);
	}

// Close the connection. 
sqlsrv_close( $conn );

?>