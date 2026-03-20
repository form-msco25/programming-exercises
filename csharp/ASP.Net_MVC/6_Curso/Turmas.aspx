<%@ Page Title="Turmas" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Turmas.aspx.cs" Inherits="Ex6.Turmas" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Gerir Turmas</h2>
        <% Obter_Dados(); %>
        <br /><br />
        <h3>Adicionar Turma</h3>
        <asp:Label ID="lbl_turma" runat="server" Text="Turma: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_turma" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Button ID="btn_inserirTurma" runat="server" Text="Inserir Turma" OnClick="btn_inserirTurma_Click" />
    </main>
</asp:Content>