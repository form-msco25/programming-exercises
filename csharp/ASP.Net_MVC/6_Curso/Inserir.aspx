<%@ Page Title="Inserir" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Inserir.aspx.cs" Inherits="Ex6.Inserir" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Inserir Aluno</h2>
        <br /><br />
        <asp:Label ID="lbl_nome" runat="server" Text="Nome: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_nome" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_email" runat="server" Text="E-mail: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_email" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_data_nasc" runat="server" Text="Data Nascimento: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_data_nasc" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_morada" runat="server" Text="Morada: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_morada" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_genero" runat="server" Text="Género: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_genero" runat="server"></asp:DropDownList>        
        <br /><br />
        <asp:Label ID="lbl_turma" runat="server" Text="Turma: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_turma" runat="server"></asp:DropDownList>
        <br /><br />
        <asp:Button ID="btn_inserir" runat="server" Text="Inserir" OnClick="btn_inserir_Click" />
    </main>
</asp:Content>
