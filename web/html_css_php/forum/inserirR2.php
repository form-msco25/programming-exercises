<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Notícias - MO</title>
    <!-- redirecionamento automático do utilizador ir para o index após 2 segundos -->
    <meta http-equiv="refresh" content="2; url=login2.php">
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Inserção de Posts/Notícias</h1><br/><br/>
        <?php
            include 'liga_bd.php';
            session_start();
            // Executo o SQL no meu servidor
            $sql = "INSERT INTO t_resp (id_post, id_user, texto, foto) VALUES ('$_POST[id_post]', '$_SESSION[id]', '$_POST[texto]', '$_POST[foto]')";
            //echo $sql;
            //se conseguir inserir os dados mostra a mensagem de "Registo efetuado com sucesso!"
            if(mysqli_query($ligacao, $sql)){
                echo "<h2> Resposta colocada com sucesso!</h2>";
            }
            mysqli_close($ligacao);
        ?> 
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador --><br/>
         <h3>Aguarde que vai ser redirecionado</h3>
        <a href="inserirP.php" target="_self">Voltar à Área Pessoal</a><br/><br/>
</body>
</html>