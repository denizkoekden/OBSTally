<!DOCTYPE html>
<?php

//Set your tally.xml-Location

$Tally_Config = '/opt//OBSTally/tally.xml';


/* You dont need to change anything below here */

if(isset($_POST['save']))
{
	$data=simplexml_load_file($Tally_Config);
	$data->host=$_POST['host'];
	$data->port=$_POST['port'];
	$data->pass=$_POST['pass'];
	$data->scene1=$_POST['scene1'];
	$data->scene2=$_POST['scene2'];
	$data->scene3=$_POST['scene3'];
	$data->scene4=$_POST['scene4'];
	$data->pv_tally_1=$_POST['pv_tally_1'];
	$data->pgm_tally_1=$_POST['pgm_tally_1'];
	$data->pv_tally_2=$_POST['pv_tally_2'];
        $data->pgm_tally_2=$_POST['pgm_tally_2'];
	$data->pv_tally_3=$_POST['pv_tally_3'];
        $data->pgm_tally_3=$_POST['pgm_tally_3'];
	$data->pv_tally_4=$_POST['pv_tally_4'];
        $data->pgm_tally_4=$_POST['pgm_tally_4'];
	$handle=fopen($Tally_Config,"wb");
	fwrite($handle,$data->asXML());
	fclose($handle);
}

$data=simplexml_load_file($Tally_Config);
$host=$data->host;
$port=$data->port;
$pass=$data->pass;
$scene1=$data->scene1;
$scene2=$data->scene2;
$scene3=$data->scene3;
$scene4=$data->scene4;
$pv_tally_1=$data->pv_tally_1;
$pgm_tally_1=$data->pgm_tally_1;
$pv_tally_2=$data->pv_tally_2;
$pgm_tally_2=$data->pgm_tally_2;
$pv_tally_3=$data->pv_tally_3;
$pgm_tally_3=$data->pgm_tally_3;
$pv_tally_4=$data->pv_tally_4;
$pgm_tally_4=$data->pgm_tally_4;
?>

<head>
<style type='text/css'>
/* form elements */
label {
    display: block;
    float: center;
    width: 50px;
}
</style>
<title> OBS Tally Config </title>
</head>
<body>
<form method="post">
	<div style='text-align:left;display:inline-block;min-width:340px;'><div style='text-align:center;'>
	<noscript>To use OBSTally, please enable JavaScript<br></noscript>
	<h1>OBS-Tally Config</h1>
	<a>Type in your OBS-Websocket Credentials, your trigger Scenes and the GPIOs your LEDs are connected to.</a></p></div>
	<fieldset>
	<legend>OBS-Websocket Credentials </legend>
	<label for="host">Host:</label>
    <textarea rows="1" cols="20" name="host" ><?php echo $host ?></textarea>
    <br>
	<label for="port">Port:</label>
	<textarea rows="1" cols="20" name="port"><?php echo $port ?></textarea>
    <br>
	<label for="pass">Pass:</label>
    <textarea rows="1" cols="20" name="pass" placeholder="*********"></textarea>
    <br>
	</fieldset>
	<fieldset>
	<legend> OBS Trigger Scene Configuration</legend>
	<label for="scene1">Scene1:</label>
	<textarea rows="1" cols="20" name="scene1"><?php echo $scene1 ?></textarea>
    <br>
        <label for="scene2">Scene2:</label>
        <textarea rows="1" cols="20" name="scene2"><?php echo $scene2 ?></textarea>
    <br>
        <label for="scene3">Scene3:</label>
        <textarea rows="1" cols="20" name="scene3"><?php echo $scene3 ?></textarea>
    <br>
        <label for="scene4">Scene4:</label>
        <textarea rows="1" cols="20" name="scene4"><?php echo $scene4 ?></textarea>
    <br>
	</fieldset>
	<fieldset>
	<legend> Define LED GPIOs as PI-GPIO-Numbers (NOT Pin-Number)</legend>
        <label for="pv_tally_1">Preview Tally 1 GPIO:</label>
        <textarea rows="1" cols="20" name="pv_tally_1"><?php echo $pv_tally_1 ?></textarea>
    <br>
	<label for="pgm_tally_1">Program Tally 1 GPIO:</label>
        <textarea rows="1" cols="20" name="pgm_tally_1"><?php echo $pgm_tally_1 ?></textarea>
    <br>
	<label for="pv_tally_2">Preview Tally 2 GPIO:</label>
        <textarea rows="1" cols="20" name="pv_tally_2"><?php echo $pv_tally_2 ?></textarea>
    <br>
        <label for="pgm_tally_2">Program Tally 2 GPIO:</label>
        <textarea rows="1" cols="20" name="pgm_tally_2"><?php echo $pgm_tally_2 ?></textarea>
    <br>
	<label for="pv_tally_3">Preview Tally 3 GPIO:</label>
        <textarea rows="1" cols="20" name="pv_tally_3"><?php echo $pv_tally_3 ?></textarea>
    <br>
        <label for="pgm_tally_3">Program Tally 3 GPIO:</label>
        <textarea rows="1" cols="20" name="pgm_tally_3"><?php echo $pgm_tally_3 ?></textarea>
    <br>
	<label for="pv_tally_4">Preview Tally 4 GPIO:</label>
        <textarea rows="1" cols="20" name="pv_tally_4"><?php echo $pv_tally_4 ?></textarea>
    <br>
        <label for="pgm_tally_4">Program Tally 4 GPIO:</label>
        <textarea rows="1" cols="20" name="pgm_tally_4"><?php echo $pgm_tally_4 ?></textarea>
    <br>
	</fieldset>
    </p>
	<input type="submit" name="save" value="Save">
</form>

</p>
<div style='text-align:right;font-size:11px;'><a href='https://github.com/denizkoekden' target='_blank'>(c) 2020 -  OBSTally by Deniz K.</a></div></div>
</body>
