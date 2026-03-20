<%-- 
    Document   : IMC
    Created on : 16/01/2026, 16:24:33
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Cálculo do IMC - MO</title>
    </head>
    <body>
        <h1>Calculadora IMC</h1>        
        <section> 
            <% 
                // 1. Recuperar os dados enviados pelo formulário
                String strPeso = request.getParameter("peso"); 
                String strAltura = request.getParameter("altura"); 
                String genero = request.getParameter("genero");

                if (strPeso != null && strAltura != null && genero != null) { 
                    try { 
                        // 2. Converter os valores para números double 
                        double peso = Double.parseDouble(strPeso.replace(",", ".")); 
                        double altura = Double.parseDouble(strAltura.replace(",", "."));

                        // 3. Aplicar a fórmula: IMC = Peso / (Altura * Altura) 
                        double imc = peso / (altura * altura); 
                        String classificacao = "";

                        // 4. Lógica de classificação baseada na tabela da atividade 
                        if (genero.equals("mas")) { 
                            if (imc < 20) classificacao = "Baixo do Peso";
                            else if (imc <= 25) classificacao = "Normal"; 
                            else if (imc <= 30) classificacao = "Acima do Peso"; 
                            else classificacao = "Obesidade"; 
                        }else { // Feminino 
                            if (imc < 19) classificacao = "Baixo do Peso"; 
                            else if (imc <= 24) classificacao = "Normal"; 
                            else if (imc <= 30) classificacao = "Acima do Peso"; 
                            else classificacao = "Obesidade"; 
                        } 

                        // 5. Exibir os resultados 
                        out.print("<p>Seu IMC é: <strong>" + String.format("%.2f", imc) + "</strong></p>"); 
                        out.print("<p>Classificação: <strong>" + classificacao + "</strong></p>"); 

                    } catch (Exception e) { 
                        out.print("<p style='color:red;'>Erro: Por favor, insira valores numéricos válidos.</p>");  
                    } 
                } 
            %>
            <br/> 
            <a href="imc.html">Voltar para o formulário</a> 
        </section> 
        <footer> 
            <p>Postado por: Michael Ortiz</p> 
        </footer> 
    </body>
</html>
