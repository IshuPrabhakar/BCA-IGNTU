<?php
    // write a program in php to find first non- repeating character in given string
    $str = "Hey there";

    $str = array_split($str);

    $arr = array_count_values($str);

    foreach ($arr as $key => $value) {
        if($value == 1){
            echo $key;
            break;
        }
    }
?>