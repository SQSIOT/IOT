<head>
<meta http-equiv="refresh" content="60"/>
</head>

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
                                }
                }

For ($i=0; $i<=(count($SQLData)-1); $i++)
{
                                // create a new cURL resource
								$l1 = '0';
								$l2 = '0';
								$l3 = '0';
								$l4 = '0';
                                
								$ch = curl_init();
                                
								$A1 = "pic_bulboff.gif";
								$A2 = "pic_bulboff.gif";
								$A3 = "pic_bulboff.gif";
								$A4 = "pic_bulboff.gif";
								
								$IP = 'http://192.168.163.150:8080/';
								
								if ($SQLData[$i]['0'] === 'ON')
								{
									$A1 = "pic_bulbon.gif";
									$l1 = '1';
								}

								if ($SQLData[$i]['1'] === 'ON')
								{
									$A2 = "pic_bulbon.gif";
									$l2 = '1';
								}

							
								if ($SQLData[$i]['2'] === 'ON')
								{
									$A3 = "pic_bulbon.gif";
									$l3 = '1';
								}

								if ($SQLData[$i]['3'] === 'ON')
								{
									$A4 = "pic_bulbon.gif";
									$l4 = '1';
								}

								$URL = $IP.$l1.$l2.$l3.$l4;
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

<!DOCTYPE html>
<meta charset="utf-8"/>
<html>
<center>
<h1>IOT Home Automation </h1><br>
<h1>By SQS India</h1>
</center>
<style>

#container {
    text-align: center;
}
a, figure {
    display: inline-block;
}

</style>
<div id="container">
    <a href="#">

<figure>
<figcaption>light 1</figcaption>
<img id="LED1" onclick="changeImage('LED1')" src="<?php echo $A1; ?>" width="100" height="180"/>
</figure>
</a>
	<a href="#">
<figure>
<figcaption>light 2</figcaption>
<img id="LED2" onclick="changeImage('LED2')" src="<?php echo $A2; ?>" width="100" height="180"/>
</figure>
</a>
	<a href="#">
<figure>
<figcaption>light 3</figcaption>
<img id="LED3" onclick="changeImage('LED3')" src="<?php echo $A3; ?>" width="100" height="180"/>
</figure>
</a>
	<a href="#">
<figure>
<figcaption>light 4</figcaption>
<img id="LED4" onclick="changeImage('LED4')" src="<?php echo $A4; ?>" width="100" height="180">
</figure>
</a>
<!--
	<a href="#">
<figure>
<figcaption>ALL LIGHT</figcaption>
<img id="LED" onclick="changeImage('LED')" src="<?php echo $A5; ?>" width="100" height="180">
</figure>
</a> 
-->
</div>

<script>
function changeImage(id) {
    var image = document.getElementById(id);
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) 
		{
            alert(xmlhttp.responseText);
        }
    };
    if (image.src.match("bulbon")) {
        image.src = "pic_bulboff.gif";
		xmlhttp.open("GET", "test.php?value="+id+"=OFF", true);
		xmlhttp.send();
	}
    else {
        image.src = "pic_bulbon.gif";
	    xmlhttp.open("GET", "test.php?value="+id+"=ON", true);
		xmlhttp.send();
	}
}

</script>
</body>
</html>