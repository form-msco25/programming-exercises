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
        <h1>Listar Manuais</h1><br/><br/>
        <?php
        include 'liga_bd.php';
            // Executo o SQL no meu servidor
            $sql ="SELECT * FROM manuais";
            // Na variável resultado armazeno os dados da instrução executada        
            $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));
            // Criação de variável para contar os clientes
            $num_reg = 0;
            // Repete este ciclo enquanto houver linhas
            while($linha = mysqli_fetch_assoc($resultado)){
                // Echo escreve para dentro do HTML
                echo "Id: ".$linha['id']."<br/>";
                echo "Título: ".$linha['titulo']."<br/>";
                echo "Nº de páginas: ".$linha['numpag']."<br/>";
                echo "Texto descritivo: ".$linha['textdescr']."<br/>";
                echo "Peso (kb): ".$linha['pesokb']."<br/>";
                echo "Autor: ".$linha['autor']."<br/><hr/>";
                $num_reg ++;
                // = ($num_clientes = $num_clientes + 1)
            }

            echo "Nº de Manuais na base de dados -->" .$num_reg;
            mysqli_close($ligacao);
            ?>              
                <br/><br/>
                <!-- <input type="button" value="Voltar ao menu" onclick="window.history.go(-1);"> -->
                
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="index.html" target="_self">Voltar ao Início</a><br/><br/>
</body>
</html>