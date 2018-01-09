<?php 
if(!$_COOKIE[user]) 
{ 
    $admin="admin"; 

    for($i=0;$i<20;$i++) 
    { 
        $admin=base64_encode($admin); 

    } 

    $admin=str_replace("1","!",$admin); 
    $admin=str_replace("2","@",$admin); 
    $admin=str_replace("3","$",$admin); 
    $admin=str_replace("4","^",$admin); 
    $admin=str_replace("5","&",$admin); 
    $admin=str_replace("6","*",$admin); 
    $admin=str_replace("7","(",$admin); 
    $admin=str_replace("8",")",$admin); 
    echo($admin)
?> 

<html>
<body>
<head>
<title>Challenge</title>
</head>
</body>
</html>