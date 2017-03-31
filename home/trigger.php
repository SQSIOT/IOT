<?php

$link=mysql_connect("192.168.162.72","obd","obd");
mysql_select_db("hauto") or die("Error:" . mysql_error());

if($link === false){
	die("Error: Could not Connect. " . mysql.connect_error());
}

$sql ="select LED1,LED2,LED3,LED4 from status";
$result = mysql_query($sql);

if($result != False)
                {
                                $SQLData = array(); 
                                while ($row = mysql_fetch_Array($result))
                                {
                                                $SQLData[] = $row;
												//print_r ($SQLData);
                                }
                }

For ($i=0; $i<=(count($SQLData)-1); $i++)
{
                                // create a new cURL resource
								$A1 = '0';
								$A2 = '0';
								$A3 = '0';
								$A4 = '0';
                                $ch = curl_init();
                                $IP = 'http://192.168.163.150:8080/';
							
								if ($SQLData[$i]['0'] === 'ON')
								{$A1 = '1';}

								if ($SQLData[$i]['1'] === 'ON')
								{$A2 = '1';}

							
								if ($SQLData[$i]['2'] === 'ON')
								{$A3 = '1';}

								if ($SQLData[$i]['3'] === 'ON')
								{$A4 = '1';}

														
								$URL = $IP.$A1.$A2.$A3.$A4;
								//print_r ($URL);

                                // set URL and other appropriate options
                                curl_setopt($ch, CURLOPT_URL, $URL);
                                curl_setopt($ch, CURLOPT_HEADER, 0);

                                // grab URL and pass it to the browser
                                curl_exec($ch);
                                
                                // close cURL resource, and free up system resources
                                curl_close($ch);
                }

// Close the connection. 
mysql_close( $link );
?>
