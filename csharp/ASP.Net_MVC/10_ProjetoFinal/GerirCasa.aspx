<%@ Page Title="Gerir Casa" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="GerirCasa.aspx.cs" Inherits="Ex10_ProjetoFinal.GerirCasa" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Gerir Casa</h2>
        <%Obter_Dados();%>
    </main>
</asp:Content>
