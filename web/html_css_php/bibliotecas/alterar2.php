<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Manuais - MO</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Editar Manuais</h1><br/><br/>
        <?php
        include 'liga_bd.php';
            // Executo o SQL no meu servidor para ir buscar os dados do cliente escolhido
            $sql ="SELECT * FROM manuais WHERE id=" .$_POST['manual'];
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));

            $linha = mysqli_fetch_assoc($resultado);
        ?>
        <form action="alterar3.php" method="post">
            <!-- Quando crio o input devo definir o type e name obrigatoriamente-->
            id: <input type="text" name="id" size="10" maxlength="10" readonly value="<?php echo $linha['id'];?>"><br/><br/>
            Título: <input type="text" name="titulo" size="40" maxlength="40" value="<?php echo $linha['titulo'];?>"><br/><br/>
            Nº de páginas: <input type="text" name="numpag" size="11" maxlength="11" value="<?php echo $linha['numpag'];?>"><br/><br/>
            Texto descritivo: <br/>
            <textarea name="textdescr" cols="80" rows="4">
                <?php echo $linha['textdescr'];?>
            </textarea>><br/><br/>
            Peso (KB): <input type="text" name="pesokb" size="6" maxlength="6" value="<?php echo $linha['pesokb'];?>"><br/><br/>
            Autor: <input type="text" name="autor" size="20" maxlength="20" value="<?php echo $linha['autor'];?>"><br/><br/>
            <input type="submit" value="Alterar"><br/><br/>            
        </form>
        <?php
            mysqli_close($ligacao);
        ?>
        <br/><br/>
        <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>