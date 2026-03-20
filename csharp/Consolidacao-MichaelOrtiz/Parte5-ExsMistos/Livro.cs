using System;
using System.Collections.Generic;
using System.Text;

namespace Parte5_ExsMistos
{
    public class Livro
    {
        public string Titulo {  get; set; }
        public string Autor { get; set; }
        public int Ano { get; set; }

        public Livro(string titulo, string autor, int ano)
        {
            Titulo = titulo;
            Autor = autor;
            Ano = ano;
        }
    }
}
