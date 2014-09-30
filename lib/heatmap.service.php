<?php

// Params
$size = $_REQUEST['size'];
$bounds = $_REQUEST['bounds'];
$data = [$size, $bounds];

#echo escapeshellarg(json_encode($data));

// Exec python script to process heatmap
$result = shell_exec("python heatmap.service.py " . escapeshellarg(json_encode($data)));

// Decode the result
echo $result;

?>