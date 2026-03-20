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
    <meta http-equiv="refresh" content="5;url:index.html">
</head>
<body>
    <?php
            // início a sessão
            session_start();
            // esvazio todas as variáveis de sessão
            $_SESSION=array();
            // destruo a sessão criada
            session_destroy();            
    ?>            
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Forum dos Programadores</h1>
        <br/><br/> <!-- Tag só de fecho -->
        <h2>Sessão terminada com sucesso.</h2>
        <br><br>
        <h4>Aguarde que vai ser redirecionado.</h4>

        <a href="index.html">Voltar ao Início.</a><br><br>
        <!-- <input type="button" value="Editar Perfil" onclick="">-->        

            <!-- <a href="editarPerfil.php">Editar Perfil</a>
            <a href="inserirP.php">Inserir Post/Notícia</a>
            <a href="listarP.php">Listar Post/Notícia</a>
            <a href="meusP.php">Meus Posts/Notícias</a>
            <a href="minhasR.php">Minhas Respostas</a>
            <a href="logout.php">Terminar Sessão</a>-->
</body>
</html>