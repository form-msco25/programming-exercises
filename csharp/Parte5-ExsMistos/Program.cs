using System.Collections;
using System.Runtime.Intrinsics.X86;
using System.Text;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Parte5_ExsMistos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ex.19
            /*Cria uma classe Pessoa com:
                Nome
                Idade
                Cria uma lista de várias pessoas e usa Where para mostrar apenas as que têm mais de 18 anos.*/
            /*List<Pessoa> pessoas = new List<Pessoa>
            {
                new Pessoa { Nome = "Michael", Idade = 32 },
                new Pessoa { Nome = "Steven", Idade = 23 },
                new Pessoa { Nome = "Cataño", Idade = 17 },
                new Pessoa { Nome = "Ortiz", Idade = 25 }
            };
            var maiorIdade = pessoas.Where(p => p.Idade > 18);
            foreach (var p in maiorIdade)
            {
                Console.WriteLine($"{p.Nome} - {p.Idade} anos");
            }*/
            //Ex.20
            /*Cria uma lista de palavras.
                Usa Select para criar uma nova lista onde todas as palavras terminam com "!".
                Exemplo:
                Olá
                Tudo
                Bem
                Resultado:
                Olá!
                Tudo!
                Bem!*/
            /*List<string> palavras = new List<string> { "Olá", "Tudo", "Bem" };
            var palavrasList = palavras.Select(p => p + "!");
            foreach (var palavra in palavrasList)
            {
                Console.WriteLine(palavra);
            }*/
            //Ex.21
            /*Cria uma lista de números.
                Ordena - os com OrderByDescending.*/
            /*List<int> numeros = new List<int> { 2, 5, 4, 1, 3 };
            var numOrdem = numeros.OrderByDescending(n => n);
            foreach (int num in numOrdem)
            {
                Console.Write(num + " ");
            }*/
            //Ex.22
            /*Cria um programa que:
                Cria uma lista de números.
                Filtra apenas os pares(Where).
                Soma esses números(Sum).*/
            /*List<int> numeros = new List<int> { 1, 2, 3, 4, 5 };
            var numPar = numeros.Where(n => n % 2 == 0);
            Console.WriteLine($"Lista números pares: ");
            foreach ( int num in numPar )
            {
                Console.Write(num + " ");
            }
            int soma = numPar.Sum();
            Console.WriteLine($"\n\nA soma dos valores é {soma}");*/
            //Ex.23
            /*Utiliza StringBuilder para construir uma frase com os nomes de uma lista de pessoas separados por vírgula.*/
            /*StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 5; i++)
            {
                if (i < 4)
                {
                    Console.WriteLine("\nInsira um nome: ");
                    sb.Append(Console.ReadLine() + ", ");
                }
                else
                {
                    Console.WriteLine("\nInsira um nome: ");
                    sb.Append(Console.ReadLine());
                }
            }
            Console.WriteLine(sb);*/
            //Ex.24
            /*Cria uma classe Livro com:
                Titulo
                Autor
                Ano
            Cria uma lista de livros e usa OrderBy para ordenar pelo ano.*/
            /*List<Livro> listaLivros = new List<Livro>
            {
                new Livro("Dom Quixote", "Miguel de Cervantes", 1605),
                new Livro("Orgulho e Preconceito", "Jane Austen", 1813),
                new Livro("Frankenstein", "Mary Shelley", 1818),
                new Livro("As Aventuras de Pinóquio", "Carlo Collodi", 1883),
                new Livro("O Velho e o Mar", "Ernest Hemingway", 1952)
            };
            var anoOrdem = listaLivros.OrderBy(l => l.Ano);
            foreach (var livro in anoOrdem)
            {
                Console.WriteLine($"{livro.Titulo} - {livro.Autor} ({livro.Ano})");
            }*/
            //Ex.25
            /*Cria uma classe Produto com:
                Nome
                Preco
            Cria uma lista de produtos.
                Depois:
                Filtra os produtos com preço maior que 100(Where)
                Ordena pelo preço(OrderBy)
                Mostra o nome e preço de cada produto.*/
            /*List<Produto> listaProdutos = new List<Produto>
            {
                new Produto { Nome = "TV", Preco = 299.00m},
                new Produto { Nome = "PC", Preco = 999.00m},
                new Produto { Nome = "Laptop", Preco = 799.00m},
                new Produto { Nome = "Rato", Preco = 49.00m},
                new Produto { Nome = "Teclado", Preco = 29.00m}
            };
            var maior = listaProdutos.Where(p => p.Preco > 100);
            var maiorOrdem = maior.OrderBy(p => p.Preco);
            foreach ( var produto in maiorOrdem )
            {
                Console.WriteLine($"Nome: {produto.Nome} | Preço: {produto.Preco} ");
            }*/
        }
    }
}
