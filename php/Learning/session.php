<?php

    $a = array("hi", "bro");

    setcookie("test", $a ,0,"");

    if(isset($_COOKIE['test'])){
        echo $_COOKIE['test'];
    }
    else
    echo "Not set";
?>