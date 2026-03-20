using System;
using System.Collections.Generic;
using System.Text;

namespace Biblioteca_C_
{
    public class Revista : Livro
    {
        private int edicao;
        public int Edicao
        {
            get { return edicao; }
            set 
            {
                if (value < 0)
                    throw new ArgumentException("Edição deve ser maior que 0.");
                edicao = value;               
            }
        }
        public Revista(string titulo, string autor, int anoPublicacao, int edicao) : base(titulo, autor, anoPublicacao)
        {
            Edicao = edicao;
        }
        public void AtualizarEdicao()
        {
            Edicao++ ;
        }
        public override string ToString()
        {
            string estado = Disponivel ? "Disponível" : "Emprestado";
            return $"\nTítulo: {Titulo} | Autor: {Autor} | Ano de publicação: {AnoPublicacao} | Estado: {estado} | Edição: {edicao}";
        }
    }
}