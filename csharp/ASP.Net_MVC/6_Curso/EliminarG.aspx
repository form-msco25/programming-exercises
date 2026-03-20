<%@ Page Title="EliminarG" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EliminarG.aspx.cs" Inherits="Ex6.EliminarG" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Eliminar Género</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_genero" runat="server" Text="Género: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_genero" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Button ID="btn_eliminarGenero" runat="server" Text="Eliminar Genero" OnClick="btn_eliminarGenero_Click" />
    </main>
</asp:Content>
