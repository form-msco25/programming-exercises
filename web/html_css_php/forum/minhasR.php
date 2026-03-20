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
        <h1>Gestão de Respostas</h1><br/><br/>
        <?php
        include 'liga_bd.php';
        session_start();
            // Executo o SQL no meu servidor
            $sql ="SELECT * FROM t_resp WHERE id_user=".$_SESSION['id'];
            // Na variável resultado armazeno os dados da instrução executada
            // no servidor ligação        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));
            // Criação de variável para contar os posts
            $num_resp = 0;
            // e posts bloqueados
            $num_resp_bloq = 0;
            // Repete este ciclo enquanto houver linhas
            while($linha = mysqli_fetch_assoc($resultado)){
                //verificar se a resposta está apagado
                if($linha['apagado']==1){
                    echo "<font color='red'>";
                // Echo escreve para dentro do HTML
                echo "Id: ".$linha['id']."<br/>";                
                echo "Texto: ".$linha['texto']."<br/>";                
                echo "Foto: <br><img height='100' src='".$linha['foto']."'<br/>";
                }
                // caso a resposta esteja ativo
                if($linha['apagado']==0){
                    echo "<form method='post' action='bloquearR.php'>";
                    echo "<input type='hidden' name='id_resp' value='".$linha['id']."'>";
                    echo "<input type='submit' value='Bloquear'></form>";
                }
                else{
                    echo "<form method='post' action='desbloquearR.php'>";
                    echo "<input type='hidden' name='id_resp' value='".$linha['id']."'>";
                    echo "<input type='submit' value='Desbloquear'></form>";
                    echo "</font>";
                }
                echo "<hr/>";
                $num_resp ++;
                // = ($num_reg = $num_reg + 1)
            }

            echo "<h3>Nº de Respostas na base de dados: ".$num_resp. "</h3>"; 
            mysqli_close($ligacao);
        ?>              
        <br/><br/>
        <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="login2.php" target="_self">Voltar</a><br/><br/>
</body>
</html>