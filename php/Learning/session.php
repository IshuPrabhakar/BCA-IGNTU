<?php

    $a = array("hi", "bro");

    setcookie("test", "fd" ,0,"");

    if(isset($_COOKIE['test'])){
        echo $_COOKIE['test'];
    }
    else
    echo "Not set";
?>