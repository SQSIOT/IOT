<!doctype html>

<html>
<head>
<meta charset="utf-8">
</head>
<body>

<a href="javascript:void(0)" onClick="updateId('LED1')">LEDON</a><br>
<a href="javascript:void(0)" onClick="updateId('LEd2')">LEDOFF</a><br>
<a href="javascript:void(0)" onClick="updateId('LED3')">LEDON</a><br>
<a href="javascript:void(0)" onClick="updateId('LED4')">LEDOFF</a><br>
<a href="javascript:void(0)" onClick="updateId('LED')">LEDON</a>
</body>
</html>

<script>

function updateId(value)
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) 
        {
            alert(xmlhttp.responseText);
        }
    };
    xmlhttp.open("GET", "test.php?value=" +value, true);
    xmlhttp.send();
}

</script>