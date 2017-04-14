<?php
session_start();
$_SESSION['login_user'] = "";
header("Location: index1.php");
?>