<?php
    $servidor="127.0.0.1";
    $user="root";
    $senha="";
    $bd="bd_forum0082";
    //para criar a variavel $ligacao necessito de 4 parametros
    //ip do servidor, nome de utilizador, senha e base_dados
    $ligacao = mysqli_connect($servidor,
        $user,$senha,$bd);
    if ($ligacao->connect_error) 
        die(mysqli_error($ligacao));
    ?>
   