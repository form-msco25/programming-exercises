<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Clientes - MO</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Editar Clientes</h1><br/><br/>
        <?php
            // O 1º é o ip do servidor ou nome, o 2º o username, 3º a senha e 4º a base de dados
            $ligacao=mysqli_connect("localhost", "root", "", "bd_0001");
            if ($ligacao->connect_error){
                die (mysqli_error($ligacao));
            }
            // Executo o SQL no meu servidor para ir buscar os dados do cliente escolhido
            $sql ="SELECT * FROM t_cliente WHERE id=" .$_POST['cliente'];
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));

            $linha = mysqli_fetch_assoc($resultado);
        ?>
        <form action="alterar3.php" method="post">
            <!-- Quando crio o input devo definir o type e name obrigatoriamente-->
            id: <input type="text" name="id" size="10" maxlength="10" readonly value="<?php echo $linha['id'];?>"><br/><br/>
            Nome: <input type="text" name="nome" size="80" maxlength="100" value="<?php echo $linha['nome'];?>"><br/><br/>
            Morada: <input type="text" name="morada" size="80" maxlength="100" value="<?php echo $linha['morada'];?>"><br/><br/>
            Zona: <input type="text" name="zona" size="30" maxlength="30" value="<?php echo $linha['zona'];?>"><br/><br/>
            NIF: <input type="text" name="nif" size="9" maxlength="9" value="<?php echo $linha['nif'];?>"><br/><br/>
            Volume de faturação: <input type="text" name="vol_fatur" width="10" maxlength="10" value="<?php echo $linha['vol_fatur'];?>"><br/><br/>
            <input type="submit" value="Alterar"><br/><br/>            
        </form>
        <?php
            mysqli_close($ligacao);
        ?>
        <br/><br/>
        <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);">     
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>