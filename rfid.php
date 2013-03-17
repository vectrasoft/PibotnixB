<?php
$page = $_SERVER['PHP_SELF'];
?>
<html>
<head>
<meta http-equiv="refresh" content="10"; URL='<?php echo $page?>'">
<title>Find RFID Points</title>
</head>


<link rel="stylesheet" href="http://livebots.cc/Ink/css/ink.css">

<script src="http://livebots.cc/Scripts/jquery-1.7.1.min.js"></script>

<script>
$(document).ready(function(){
  $("button").click(function(){
    $.post("http://livebots.cc/API/SetMessage",
    {
      Message:$(this).attr('value'),
      RobotId:30
    });
  });
});
</script>

<body style="background-color: transparent">

<table border="0">
        <tr>
            <td style="width: 33%; text-align: center; height:40">
            </td>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Forward" title="Forward" style="width: 90%">Forward</button>
            </td>
            <td style="width: 33%; text-align: center; height:40">
            </td>
        </tr>
        <tr>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Left" title="Left" style="width: 90%">Left</button>
            </td>
            <td style="width: 33%; text-align: center; height:40">
            </td>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Right" title="Right" style="width: 90%">Right</button>
            </td>
        </tr>
        <tr>
            <td style="width: 33%; text-align: center; height:40">
            </td>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Backward" title="Backward" style="width: 90%">Backward</button>
            </td>
            <td style="width: 33%; text-align: center; height:40">
            </td>
        </tr>
        <tr>
            <td style="width: 33%; text-align: center; height:40">
            </td>
            <td style="width: 33%; text-align: center; height:40">
            </td>
            <td style="width: 33%; text-align: center; height:40">
            </td>
        </tr>
        <tr>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Look Left" title="Look Left" style="width: 90%">Look Left</button>
            </td>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Look Forward" title="Look Forward" style="width: 90%">Look Forward</button>
            </td>
            <td style="width: 33%; text-align: center; height:40">
                <button id="Message" name="Message" class="ink-button " value="Look Right" title="Look Right" style="width: 90%">Look Right</button>
            </td>
        </tr>
</table>



<?php
$pointsFile = '/home/pi/pibotnixb/points';
if (file_exists($pointsFile)) {
	$fh = fopen($pointsFile,'r');
	$thePoints = fread($fh,filesize($pointsFile));
	fclose($fh);
	echo "You found ",$thePoints," points!";
} else {
	echo "You have not found any points yet";
}
?>

</body>
</html>
