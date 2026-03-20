<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Utilizadores - MO</title>
    <!-- redirecionamento automático do utilizador ir para o index após 2 segundos -->
    <meta http-equiv="refresh" content="2; url=index.html">
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Desbloqueio de Utilizadores</h1><br/><br/>
        <?php
            include 'liga_bd.php';
            // Executo o SQL no meu servidor
            $sql = "UPDATE t_user SET apagado=0 WHERE id=$_POST[id_user]";
            //echo $sql;
            //se conseguir inserir os dados mostra a mensagem de "Cliente inserido com sucesso"
            if(mysqli_query($ligacao, $sql)){
                echo "<h2> Utilizador desbloqueado com sucesso!</h2>";
            }
            mysqli_close($ligacao);
        ?>
            <h3> Aguarde que vai ser redirecionado...</h3>
        <br/>                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador --><br/>
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>