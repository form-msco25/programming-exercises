using System;
using System.Collections.Generic;
using System.Text;

namespace Biblioteca_C_
{
    public class Biblioteca
    {
        private string nome;
        private List<Livro> listaLivros;
        private string[] funcionarios;
        
        public Biblioteca(string nome) 
        { 
            this.nome = nome;
            listaLivros = new List<Livro>();
            funcionarios = new string[3];
        }
        public void AdicionarLivro(Livro livro)
        {
            listaLivros.Add(livro);
            Console.WriteLine("Livro adicionado com sucesso.");
        }
        public void ListarLivros()
        {
            if (listaLivros.Count == 0)
            {
                Console.WriteLine("Não existem livros na biblioteca.");
                return;
            }
            Console.WriteLine($"Livros da biblioteca {nome}: ");
            foreach (Livro livro in listaLivros)
            {
                Console.WriteLine(livro);
            }
        }
        public void InputFuncionarios()
        {
            for (int i = 0; i < funcionarios.Length; i++)
            {
                Console.Write($"Introduza o nome do funcionário {i + 1}: ");
                funcionarios[i] = Console.ReadLine();
            }
        }
        public void ListarFuncionarios()
        {
            Console.WriteLine("Funcionários da biblioteca: ");
            for (int i = 0; i < funcionarios.Length; i++)
            {
                Console.WriteLine($"\n{i + 1} - {funcionarios[i]}");
            }
        }
    }
}
