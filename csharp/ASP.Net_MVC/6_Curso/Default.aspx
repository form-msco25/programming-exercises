 <%@ Page Title="Página Inicial" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Ex6._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">

    <main>
        <section class="row" aria-labelledby="aspnetTitle">
            <h1 id="aspnetTitle">Gestão de Alunos</h1>
            <p class="lead">Esta aplicação feita em ASP.Net usa HTML, CSS e JavaScript.</p>            
        </section>
        <p style="text-align:center">
            <img alt="Imagem de uma turma" src="https://simulare.com.br/wp-content/uploads/como-usar-a-tecnologia-na-sala-de-aula-descubra-aqui.jpg" />
        </p>
        <div class="row">
            <section class="col-md-4" aria-labelledby="gettingStartedTitle">
                <h2 id="gettingStartedTitle">Gestão de Alunos</h2>
                <p>
                    A gestão de alunos é composta por um form que contém uma listagem simples,
                    um form para inserir dados e outro form que permite gerir (ou seja, editar e eliminar alunos)
                </p>
                <p>
                    <a class="btn btn-default" href="Gerir.aspx">Ler mais &raquo;</a>
                </p>
            </section>
            <section class="col-md-4" aria-labelledby="librariesTitle">
                <h2 id="librariesTitle">Gestão de Turmas</h2>
                <p>
                    A gestão de turmas permite visualizar as turmas existentes, bem como adicionar e apagar turmas.
                </p>
                <p>
                    <a class="btn btn-default" href="Turmas.aspx">Ler mais &raquo;</a>
                </p>
            </section>
            <section class="col-md-4" aria-labelledby="hostingTitle">
                <h2 id="hostingTitle">Gestão de Géneros</h2>
                <p>
                    A gestão de géneros permite visualizar os géneros existentes, bem como adicionar e apagar géneros.
                </p>
                <p>
                    <a class="btn btn-default" href="Generos.aspx">Ler mais &raquo;</a>
                </p>
            </section>
        </div>
    </main>
</asp:Content>