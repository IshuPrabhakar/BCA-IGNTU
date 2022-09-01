
<?php
    // Write a program in php to remove specific element by value from the array

    $arr = array(1 => "hey", 2 => "hi", 3 => "hello");

    // to remove specific element from the array we use unset()
    unset($arr[3]);

    print_r($arr);
?>