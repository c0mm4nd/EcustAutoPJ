<?php 
$pw = $_GET['pw'];
$id = $_GET['id'];
print passthru('python pj.py '.$id.'x'.$pw);

 ?>
