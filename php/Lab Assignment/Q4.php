<?php
    // write a function to find a specified value of associative array within a function
    function search($arr, $key){

        for ($i=0; $i < count($arr); $i++) { 
                if($arr[$i] == $value)
                    return $i;
        }
    }
?>