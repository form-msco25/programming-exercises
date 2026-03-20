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
        <h1>Gestão de Utilizadores</h1><br/><br/>
        <?php
        include 'liga_bd.php';
            // Executo o SQL no meu servidor
            $sql ="SELECT * FROM t_user";
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));
            // Criação de variável para contar os clientes
            $num_reg = 0;
            // Repete este ciclo enquanto houver linhas
            while($linha = mysqli_fetch_assoc($resultado)){
                // Echo escreve para dentro do HTML
                echo "Id: ".$linha['id']."<br/>";
                echo "Nick: ".$linha['nick']."<br/>";
                echo "Nome: ".$linha['nome']."<br/>";
                echo "E-mail: ".$linha['email']."<br/>";
                echo "Data de nascimento: ".$linha['data_nasc']."<br/>";
                echo "Foto: <br><img height='100' src='".$linha['foto']."'<br/>";
                    if ($linha['apagado']==0){
                        echo "<form method='post' action='apagar_u.php'>";
                        echo "<input type='hidden' name='id_user' value='".$linha['id']."'>";
                        echo "<input type='submit' value='Apagar'></form>";
                    }
                    else {
                        echo "<form method='post' action='recuperar_u.php'>";
                        echo "<input type='hidden' name='id_user' value='".$linha['id']."'>";
                        echo "<input type='submit' value='Recuperar'></form>";
                    }
                echo "<form method='post' action='alterar_u.php'>";
                echo "<input type='hidden' name='id_user' value='".$linha['id']."'>";
                echo "<input type='submit' value='Alterar'></form>";

                echo "<hr/>";
                $num_reg ++;
                // = ($num_reg = $num_reg + 1)
            }

            echo "<h3>Nº de registos na base de dados -->" .$num_reg . "</h3>"; 
            mysqli_close($ligacao);
            ?>              
                <br/><br/>
                <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>