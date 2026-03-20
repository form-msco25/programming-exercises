<%@ Page Title="Gerir Cliente" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="GerirCliente.aspx.cs" Inherits="Ex10_ProjetoFinal.GerirCliente" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Gerir Cliente</h2>
        <%Obter_Dados();%>
    </main>
</asp:Content>
