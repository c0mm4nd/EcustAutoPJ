<?php 
$pw = $_GET['pw'];
$id = $_GET['id'];
print passthru('C:/Python27/python.exe  pj.py '.$id.'x'.$pw);

 ?>
