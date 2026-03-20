<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Clientes - MO</title>
    <!-- redirecionamento automático do utilizador ir para o index após 2 segundos -->
    <meta http-equiv="refresh" content="2; url=index.html">
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Alteração de Clientes</h1><br/><br/>
        <?php
            // O 1º é o ip do servidor ou nome, o 2º o username, 3º a senha e 4º a base de dados
            $ligacao=mysqli_connect("localhost", "root",  "", "bd_0001");
            // verifica se a ligação é feita com sucesso
            if ($ligacao->connect_error){
                die (mysqli_error($ligacao));
            }
            // Executo o SQL no meu servidor
            $sql = "UPDATE t_cliente SET nome='$_POST[nome]', morada='$_POST[morada]', zona='$_POST[zona]', nif='$_POST[nif]', vol_fatur=$_POST[vol_fatur] WHERE id=$_POST[id]";
            //echo $sql;
            //se conseguir inserir os dados mostra a mensagem de "Cliente inserido com sucesso"
            if(mysqli_query($ligacao, $sql)){
                echo "<h2> Cliente alterado com sucesso!</h2>";
            }
            mysqli_close($ligacao);
        ?> 
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador --><br/>
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>