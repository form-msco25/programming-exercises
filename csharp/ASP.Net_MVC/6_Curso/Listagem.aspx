<%@ Page Title="Listagem Alunos" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Listagem.aspx.cs" Inherits="Ex6.Listagem" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Listagem de alunos</h2>
        <% Lista_dados(); %>
        
    </main>
</asp:Content>
