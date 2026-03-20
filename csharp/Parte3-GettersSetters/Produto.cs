using System;
using System.Collections.Generic;
using System.Text;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Parte3_GettersSetters
{
    public class Produto
    {
        //Ex10
        /*Cria uma classe Produto com duas propriedades:
            Nome
            Preco
            Cria um objeto e mostra os valores no ecrã.*/
        public string Nome { get; set; }
        public decimal Preco { get; set; }

    }
}
