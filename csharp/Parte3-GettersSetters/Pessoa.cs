using System;
using System.Collections.Generic;
using System.Runtime.Intrinsics.X86;
using System.Text;

namespace Parte3_GettersSetters
{
    public class Pessoa
    {
        //Ex9.
        /*Cria uma classe chamada Pessoa com uma propriedade:
            Nome
            Cria um objeto da classe e atribui um nome.
            Mostra o nome no ecrã.*/
        //public string Nome { get; set; }
        private string nome;

        public string Nome
        {
            get { return nome; }
            set { nome = value; }
        }
    }
}
