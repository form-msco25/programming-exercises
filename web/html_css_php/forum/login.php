<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Notícias - MO</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Forum dos Programadores</h1>
        <br/><br/> <!-- Tag só de fecho -->
        <?php
            include 'liga_bd.php';
            // crio a instrução para ir buscar os dados do user
            $sql ="SELECT * FROM t_user WHERE nick='" .$_POST['nick']."'";
            // crio o array resultado que vai armazenar os dados pesquisados
            $resultado = mysqli_query($ligacao, $sql);
            // cria a variável linha para ver se consigo obter os daos
            $linha = mysqli_fetch_assoc($resultado);
            // caso o utilizador não exista
            if ($linha == NULL)
                header('Location: erro.html');
            // verificar se a senha colocada é igual à da base de dados
            if(strcmp($linha['pass'], $_POST['senha'])==0){
                session_start();
                $_SESSION['id']=$linha['id'];
                $_SESSION['nick']=$linha['nick'];
                header('Location: login2.php');
            }
            else
                // caso a senha esteja errada
                header('Location: erro.html');
        ?>        
</body>
</html>