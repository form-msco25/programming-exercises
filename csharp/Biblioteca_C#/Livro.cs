using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace Biblioteca_C_
{
    public class Livro
    {
        // atributos
        private string titulo;
        private string autor;
        private int anoPublicacao;
        private bool disponivel;
        //propriedades
        public string Titulo
        {
            get { return titulo; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("O título não pode ser vazio.");
                titulo = value;
            }
        }
        public string Autor
        {
            get { return autor; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("O autor não pode ser vazio.");
                autor = value;
            }
        }
        public int AnoPublicacao
        {
            get { return anoPublicacao; }
            set
            {
                if (value < 1450)
                    throw new ArgumentException("O ano de publicação não pode ser inferior a 1450.");
                anoPublicacao = value;
            }
        }
        public bool Disponivel
        {
            get { return disponivel; }
            private set { disponivel = value; }
        }
        // contrutor
        public Livro(string titulo, string autor, int anoPublicacao)
        {
            Titulo = titulo;
            Autor = autor;
            AnoPublicacao = anoPublicacao;
            Disponivel = true;
        }
        // métodos
        public void Emprestar()
        {
            if (Disponivel)
            {
                Disponivel = false;
            }
            else
            {
                Console.WriteLine("O livro já está emprestado.");
            }
        }
        public void Devolver()
        {
            if (Disponivel)
            {
                Console.WriteLine("O livro já está disponível");
            }
            else
            {
                Disponivel = true;
                Console.WriteLine("Livro devolvido com sucesso.");
            }
        }
        public override string ToString()
        {
            string estado = Disponivel ? "Disponível" : "Emprestado";
            return $"\nTítulo: {Titulo} | Autor: {Autor} | Ano de publicação: {AnoPublicacao} | Estado: {estado}";
        }
    }
}
