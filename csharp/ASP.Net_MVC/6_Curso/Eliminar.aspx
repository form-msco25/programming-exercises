<%@ Page Title="Eliminar" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Eliminar.aspx.cs" Inherits="Ex6.Eliminar" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Eliminar Alunos</h2>
        <br /><br />
        <asp:Label ID="lbl_numero" runat="server" Text="Número: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_numero" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_nome" runat="server" Text="Nome: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_nome" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_email" runat="server" Text="E-mail: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_email" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_data_nasc" runat="server" Text="Data Nascimento: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_data_nasc" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_morada" runat="server" Text="Morada: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_morada" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_genero" runat="server" Text="Género: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_genero" ReadOnly="true" runat="server"></asp:DropDownList>        
        <br /><br />
        <asp:Label ID="lbl_turma" runat="server" Text="Turma: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_turma" ReadOnly="true" runat="server"></asp:DropDownList>
        <br /><br />
        <asp:Button ID="btn_eliminar" runat="server" Text="Eliminar" OnClick="btn_eliminar_Click" />
    </main>
</asp:Content>
