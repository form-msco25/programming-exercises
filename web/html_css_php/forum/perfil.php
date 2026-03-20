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
    <?php
        include 'liga_bd.php';
        session_start();
        // crio a instrução sql para ir buscar os dados do user
        $sql ="SELECT * FROM t_user WHERE id=".$_SESSION['id'];
        // executo a instrução
        $resultado=mysqli_query($ligacao, $sql);
        // guardo os dados para dentro da variável linha
        $linha=mysqli_fetch_assoc($resultado);
    ?>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Alteração de Perfil</h1>
    <!-- Para enviar os dados para outra página uso a tag form action (nome da página para onde envio) methos (post para camuflar os dados)-->
    <form action="perfil2.php" method="post">
        <!-- Quando crio o input devo definir o type e name obrigatoriamente-->
        Nick: <input type="text" name="nick" size="20" maxlength="20" readonly value="<?php echo $linha['nick'];?>"><br/><br/>
        Nome: <input type="text" name="nome" size="80" maxlength="100" required value="<?php echo $linha['nome'];?>"><br/><br/>
        E-mail: <input type="email" name="email" size="50" maxlength="50" required value="<?php echo $linha['email'];?>"><br/><br/> <!-- type="email" == é obrigatório o uso de '@' e '.'-->
        Data de nascimento: <input type="date" name="data_nasc" required value="<?php echo $linha['data_nasc'];?>"><br/><br/> <!-- type="date" == formato calendário-->
        Senha: <input type="password" name="pass" size="20" maxlength="20" required value="<?php echo $linha['pass'];?>"><br/><br/> <!-- type="password" == aparece a palavra-passe oculta-->
        Foto(url): <br>
        <textarea name="foto" rows="4" cols="80"><?php echo $linha['foto'];?></textarea><br/><br/>
        <input type="submit" value="Inserir"><br/><br/>
        <input type="reset" value="Limpar"><br/><br/>
    </form>
    <br/><br/> <!-- Tag só de fecho -->
    <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
    <a href="login2.php" target="_self">Voltar à Área Pessoal</a><br/><br/>
</body>
</html>