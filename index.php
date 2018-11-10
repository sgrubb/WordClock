<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<link rel="stylesheet" href="index.css"/>

<html>
<body>
<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);



$filename = "/etc/wpa_supplicant/wpa_supplicant.conf";
$fd = fopen($filename,"r");
$textFileContents = file_get_contents($filename);
fclose($fd);

if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $textFileContents = $_POST['newdata'];
    file_put_contents($filename,str_replace("\r\n","\n",$textFileContents));
}
?>


<form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="POST" >
<div class="form-group">
<textarea font-size: 18px; class="form-control" name="newdata" rows="30">
<?php echo stripslashes($textFileContents); ?>
</textarea>
<button type="submit" class="btn btn-primary">Submit</button>
</div>
</form>
</body>
</html>

