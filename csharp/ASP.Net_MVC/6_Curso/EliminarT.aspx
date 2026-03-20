<%@ Page Title="EliminarT" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EliminarT.aspx.cs" Inherits="Ex6.EliminarT" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Eliminar Turmas</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_turma" runat="server" Text="Turma: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_turma" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Button ID="btn_eliminarTurma" runat="server" Text="Eliminar Turma" OnClick="btn_eliminarTurma_Click" />
    </main>
</asp:Content>
