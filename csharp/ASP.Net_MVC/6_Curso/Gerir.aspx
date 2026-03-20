<%@ Page Title="Gerir Alunos" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Gerir.aspx.cs" Inherits="Ex6.Gerir" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Gerir Alunos</h2>
        <%Obter_Dados();%>        
    </main>
</asp:Content>
