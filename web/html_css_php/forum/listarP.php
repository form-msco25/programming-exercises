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
        <h1>Listagem de Posts/Notícias</h1><br/><br/>
        <?php
        include 'liga_bd.php';
            // Executo o SQL no meu servidor
            $sql ="SELECT * FROM t_post WHERE apagado=0";
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));
            // Criação de variável para contar os clientes
            $num_posts = 0;
            // Repete este ciclo enquanto houver linhas
            while($linha = mysqli_fetch_assoc($resultado)){
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
                
                echo "<br>Autor: ".$linha2['nick']."</br>";
                echo "<form method='post' action='inserirR.php'>";
                echo "<input type='hidden' name='id_post' value='".$linha['id']."'>";
                echo "<input type='submit' value='Ver respostas/responder'></form>";

                echo "<hr/>";
                $num_posts ++;
                // = ($num_reg = $num_reg + 1)
            }

            echo "<h3>Nº de Posts/Notícias na base de dados: ".$num_posts. "</h3>"; 
            mysqli_close($ligacao);
        ?>              
        <br/><br/>
        <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="login2.php" target="_self">Voltar</a><br/><br/>
</body>
</html>