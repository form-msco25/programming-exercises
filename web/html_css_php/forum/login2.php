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
            session_start();
            echo "<h2> Bem-vindo " . $_SESSION['nick'] . "</h2>";
        ?>
             
        <input type="button" value="Editar Perfil" onclick="window.open('perfil.php', '_self')">
        <input type="button" value="Colocar Post/Notícias" onclick="window.open('inserirP.php', '_self')">
        <input type="button" value="Listar Post/Notícias" onclick="window.open('listarP.php', '_self')">
        <input type="button" value="Meus Post/Notícias" onclick="window.open('meusP.php', '_self')">
        <input type="button" value="Minhas_Respostas" onclick="window.open('minhasR.php', '_self')">
        <input type="button" value="Logout" onclick="window.open('logout.php','_self')">
        
        <!--
        <a href="perfil.php">Editar Perfil</a><br/><br/>
        <a href="inserirP.php">Inserir Post/Notícia</a><br/><br/>
        <a href="listarP.php">Listar Post/Notícia</a><br/><br/>
        <a href="meusP.php">Meus Posts/Notícias</a><br/><br/>
        <a href="minhasR.php">Minhas Respostas</a><br/><br/>
        <a href="logout.php">Terminar Sessão</a><br/><br/>
        -->

        <br/><br/>
        <br/><br/>

        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>