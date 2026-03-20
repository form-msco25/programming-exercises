<!DOCTYPE html>
<html lang="pt">
<head>
    <!-- para permitir caracteres pt: ç, ~, etc. -->
    <meta charset="UTF-8">
    <!-- fazer o auto ajuste para visualizações de ecrãs -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- texto que vai aparecer na barra de título do browser -->
    <title>Gestão de Posts - MO</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Listagem de Notícias com Respostas</h1><br/><br/>
        <?php
        include 'liga_bd.php';
            // Executo o SQL no meu servidor
            $sql ="SELECT * FROM t_post WHERE apagado=0 AND id=".$_POST['id_post'];
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));
            // Criação de variável para contar as respotas
            $num_resp = 0;            
            $linha = mysqli_fetch_assoc($resultado);
                // Echo escreve para dentro do HTML
                echo "Id: ".$linha['id']."<br/>";
                echo "Tema: ".$linha['tema']."<br/>";
                echo "Título: ".$linha['titulo']."<br/>";
                echo "Texto: ".$linha['texto']."<br/>";                
                echo "Foto: <br><img height='100' src='".$linha['foto']."'<br/>";                
                // echo "Autor: " .$linha['id_user']."<br>"
                $sql2 = "SELECT id, nick FROM t_user WHERE id=".$linha['id_user'];
                $resultado2=mysqli_query($ligacao, $sql2);
                $linha2=mysqli_fetch_assoc($resultado2);                
                echo "Autor: ".$linha2['nick']."</br>";
                /* Fim dos dados do post carregamento das respostas a este post */

                // th (table header - cabeçalho)
                // tr (table row - linha
                // td (table data - célula)
                echo"<table width='60%' border='1' style='text-align:center;'>";
                echo "<tr><th>Texto</th><th>Foto</th><th>Nick</th></tr>";
                $sql3= "SELECT * FROM t_resp WHERE apagado=0 AND id_post=".$_POST['id_post'];
                $resultado3 = mysqli_query ($ligacao,$sql3) or die (mysqli_error($ligacao));
                while($linha3=mysqli_fetch_assoc($resultado3)){
                    echo "<tr><td>".$linha3['texto']."</td>";
                    echo "<td><img height='50' src='".$linha3['foto']."'></td>";
                    // versão inicial que imprimia id
                    // echo "<td>".$linha3['id_user']."</td></tr>";
                    $sql4 = "SELECT id, nick FROM t_user WHERE id=".$linha['id_user'];
                    $resultado4=mysqli_query($ligacao, $sql4);
                    $linha4=mysqli_fetch_assoc($resultado4);
                    echo "<td>".$linha4['nick']."</td></tr>";                    
                    $num_resp ++;
                    // = ($num_reg = $num_reg + 1)
                }
            echo "<tr><th colspan='3'> Total de Respostas: ".$num_resp."</th></tr></table>"; 

            /* Parte 3 - form para colocar uma respostas */
        ?> 
        <h2>Inserir Resporta</h2>
        <form action="inserirR2.php" method="post">
                Texto:<br> <textarea name="texto" rows="4" cols="80"></textarea><br><br>
                Foto:<br> <textarea name="foto" rows="4" cols="80"></textarea><br><br>
                <input type="hidden" name="id_post" value="<?php echo $_POST['id_post'];?>">
                <input type="submit" value="Inserir Resposta">
        </form>
        <br/><br/>

        <?php
            mysqli_close($ligacao);
        ?>
        <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="login2.php" target="_self">Voltar</a><br/><br/>
</body>
</html>