<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Manuais - MO</title>
    <!-- redirecionamento automático do utilizador ir para o index após 2 segundos -->
    <meta http-equiv="refresh" content="2; url=index.html">
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Inserçao de Manuais</h1><br/><br/>
        <?php
        //ligar á base de dados
        include 'liga_bd.php';
        // instrução sql a ser executada
        $sql="INSERT INTO manuais (titulo, numpag, textdescr, pesokb, autor) VALUES ('$POST[titulo]','$_POST[numpag]', '$_POST[textdescr]', '$_POST[pesokb]', '$_POST[autor]')";
        
            //echo $sql;
            //se conseguir inserir os dados mostra a mensagem de "Cliente inserido com sucesso"
            if(mysqli_query($ligacao, $sql)){
                echo "<h2> Manual Inserido com sucesso!</h2>";
            }
            mysqli_close($ligacao);
        ?> 
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador --><br/>
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>