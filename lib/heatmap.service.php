<?php

// get params
$png = $_REQUEST['png'];
$dotSize = $_REQUEST['dotSize'];
$opacity = $_REQUEST['opacity'];
// $scheme = $_REQUEST['scheme'];
$imgSize = $_REQUEST['imgSize'];
$bounds = $_REQUEST['bounds'];

// prepare json
//$data = [[$dotSize, $opacity, $scheme], $imgSize, $bounds];
$data = [[$png, $dotSize, $opacity], $imgSize, $bounds];

#echo escapeshellarg(json_encode($data));

// Clear images older than 1 min
$files = glob('../imgs/*');
foreach($files as $file)
{	
	$filemtime=filemtime($file);
  	if (is_file($file) && (time()-$filemtime>= 60))
  	{
  		// delete file
		unlink($file);
	}
}

// Exec python script to process heatmap
$result = shell_exec("python heatmap.service.py " . escapeshellarg(json_encode($data)));

// Decode the result
echo $result;

?>