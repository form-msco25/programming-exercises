using System;
using System.Collections.Generic;
using System.Text;

namespace Biblioteca_C_
{
    public class Leitor
    {
        private string nome;
        private int numLeitor;
        private List<Livro> livrosEmprest;

        public string Nome
        {
            get { return nome; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("O nome não pode ser vazio.");
                nome = value;
            }
        }
        public int NumLeitor
        {
            get { return numLeitor; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("Número de leitor não pode ser negativo.");
                numLeitor = value;
            }
        }
        public Leitor(string nome, int numLeitor)
        {
            Nome = nome;
            NumLeitor = numLeitor;
            livrosEmprest = new List<Livro>();            
        }

        public void RequisitarLivro(Livro livro)
        {
            if (!livro.Disponivel)
            {
                Console.WriteLine("O livro não está disponível.");
                return;
            }
            if (livrosEmprest.Count >= 2)
            {
                Console.WriteLine("O leitor já tem o máximo de livros emprestados (2).");
                return;
            }
            livrosEmprest.Add(livro);
            livro.Emprestar();
            Console.WriteLine("Livro requisitado com sucesso.");
        }
        public void Devolver (Livro livro)
        {
            if (livrosEmprest.Contains(livro))
            {
                livrosEmprest.Remove(livro);
                livro.Devolver();
                Console.WriteLine("Livro devolvido com sucesso.");
            }
            else
            {
                Console.WriteLine("Este livro não foi requisitado por este leitor.");
            }            
        }
        public int TotalEmprest()
        {
            return livrosEmprest.Count; 
        }
        public override string ToString()
        {
            return $"Nome: {Nome} | Nº Leitor: {NumLeitor} | Livros emprestados: {TotalEmprest()}";
        }
    }
}
