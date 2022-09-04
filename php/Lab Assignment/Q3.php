<?php
    // writr a program to sort the following associative array
    // array("Sophia" => 31, "Jacob" => 41, "William" =>39, "Ramesh" => 40);

    $arr = array("Sophia" => 31, "Jacob" => 41, "William" =>39, "Ramesh" => 40);

    // Ascending order sort by value
    echo "Ascending order sort by value <br>"
    asort($arr);
    print_r($arr);

    // Ascending order by key
    echo "Ascending order sort by key <br>"
    ksort($arr);
    print_r($arr);

    // Decending order by value
    echo "Decending order by value <br>"
    arsort($arr);
    print_r($arr);

    // Decending order by key
    echo "Decending order by key <br>"
    krsort($arr);
    print_r($arr);
    
?>