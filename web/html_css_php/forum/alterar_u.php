<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Utilizadores - MO</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Alterar Utilizadores</h1><br/><br/>
        <?php
            include 'liga_bd.php';
            // Executo o SQL no meu servidor para ir buscar os dados do cliente escolhido
            $sql ="SELECT * FROM t_user WHERE id=" .$_POST['id_user'];
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));

            $linha = mysqli_fetch_assoc($resultado);
        ?>
        <form action="alterar_u2.php" method="post">
            <!-- Quando crio o input devo definir o type e name obrigatoriamente-->
            id: <input type="text" name="id" size="10" maxlength="10" readonly value="<?php echo $linha['id'];?>"><br/><br/>
            Nick: <input type="text" name="nick" size="20" maxlength="20" value="<?php echo $linha['nick'];?>"><br/><br/>
            Nome: <input type="text" name="nome" size="80" maxlength="100" value="<?php echo $linha['nome'];?>"><br/><br/>
            E-mail: <input type="email" name="email" size="50" maxlength="50" value="<?php echo $linha['email'];?>"><br/><br/>
            Data de nascimento: <input type="date" name="data_nasc" value="<?php echo $linha['data_nasc'];?>"><br/><br/>
            Senha: <input type="password" name="pass" size="20" maxlength="20" value="<?php echo $linha['pass'];?>"><br/><br/>
            Foto:<br>
            <img height="100" src="<?php echo $linha['foto'];?>"><br/><br/>            
            <textarea name="foto" rows="4" cols="80"><?php echo $linha['foto'];?></textarea><br/><br/>
            
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