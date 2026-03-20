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
        session_start();
    ?>
        <!-- Os títulos (heading) variam de 1 (maior) a 6 (menor)-->    
        <h1>Inserção de Post/Notícias</h1>
        <!-- Para enviar os dados para outra página uso a tag form action (nome da página para onde envio) methos (post para camuflar os dados)-->
        <form action="inserirP2.php" method="post">
            <!-- A linha seguinte é apenas de leitura e vai buscar o id do utilizador à-->
            Id_Utilizador: <input type="text" name="id_user" size="10" maxlength="10" readonly value="<?php echo $_SESSION['id'];?>"><br/><br/>
            <!-- Por forma a limitar os temas implementa-se um 'select' (listbox)-->
            Tema: <select name="tema">
                <option value="Desporto">Desporto</option>
                <option value="Sociedade">Sociedade</option>
                <option value="Tecnologia">Tecnologia</option>
                <option value="Educacão">Educação</option>
                <option value="Tempos Livres">Tempos Livres</option>
            </select><br/><br/>
            Título: <input type="text" name="titulo" size="50" maxlenght="50" required><br/><br/>
            Texto: <br>
            <textarea name="texto" rows="4" cols="80"></textarea><br/><br/>            
            Foto(url): <br>
            <textarea name="foto" rows="4" cols="80"></textarea><br/><br/>
            <input type="submit" value="Inserir"><br/><br/>
            <input type="reset" value="Limpar"><br/><br/>
        </form>
        <br/><br/> <!-- Tag só de fecho -->
        <!-- Ao criar a hiperligação digo o 'href' (a página a abrir) e devo indicar o target (_self) no próprio separador (_blank) num novo separador -->
        <a href="login2.php" target="_self">Voltar</a><br/><br/>
</body>
</html>