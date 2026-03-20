using System.Globalization;
using static System.Net.Mime.MediaTypeNames;

namespace Parte3_GettersSetters
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ex.9
            /*Pessoa p1 = new Pessoa();
            p1.Nome = "Michael";
            Console.WriteLine(p1.Nome);*/
            //Ex.10            
            /*Produto p1 = new Produto();
            p1.Nome = "TV";
            p1.Preco = 299.90m;
            Console.WriteLine($"Produto: {p1.Nome} | Preço: {p1.Preco} €");*/
            //Ex.11
            /*Aluno a1 = new Aluno();
            //a1.Nota = -15;
            a1.Nota = 15;
            Console.WriteLine(a1.Nota);*/
            //Ex.12
            ContaBancaria contaBancaria1 = new ContaBancaria();
            contaBancaria1.Titular = "Michael Ortiz";
            contaBancaria1.Depositar(999.55m);
            Console.WriteLine($"Titular: {contaBancaria1.Titular}");
            Console.WriteLine($"Saldo: {contaBancaria1.Saldo}€");

        }
    }
}
