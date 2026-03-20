using System.Collections;
using System.Net;
using System.Text;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Parte4_LINQ
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ex.13
            /*Cria uma lista de números:
                1,2,3,4,5,6,7,8,9,10
                Usa Where para obter apenas os números pares.
                Mostra o resultado.*/
            /*List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            var numerosPares = numeros.Where(n => n % 2 == 0);
            foreach (int num in numeros)
            {
                Console.Write(num + " ");
            }*/
            //Ex.14
            /*Cria uma lista de números:
                1,2,3,4,5
                Usa Select para criar uma nova lista com os quadrados dos números.*/
            /*List<int> numeros = new List<int> { 1, 2, 3, 4, 5 };
            var quadrados = numeros.Select(n => n * n);
            foreach (int num in quadrados)
            {
                Console.Write(num + " ");
            }*/
            //Ex.15
            /*Cria uma lista de nomes:
                Ana, Carlos, Bruno, Diana
                Ordena os nomes usando OrderBy.*/
            /*List<string> nomes = new List<string> { "Ana", "Carlos", "Bruno", "Diana" };
            var ordenados = nomes.OrderBy(n => n);
            foreach (string nome in ordenados)
            {
                Console.Write(nome + " ");
            }*/
            //Ex.16
            /*Cria uma lista de números:
                10,20,30,40
                Usa Sum para calcular o total e encontra um LINQ que te possa ajudar a fazer a média.*/
            /*List<int> numeros = new List<int> { 10, 20, 30, 40 };
            var soma = numeros.Sum();
            decimal media = (decimal)soma / numeros.Count;
            Console.WriteLine($"Soma: {soma}");
            Console.WriteLine($"Média: {media}");*/
            //Ex.17
            /*Cria uma lista de números:
                3,5,7,8,9
                Usa Any para verificar se existe algum número par.*/
            /*List<int> numeros = new List<int> { 3, 5, 7, 8, 9 };
            bool existeNumPar = numeros.Any(n => n%2  == 0);
            if (existeNumPar){Console.WriteLine("Existe número par.");}
            else { Console.WriteLine("Não existe número par."); }*/
            //Ex.18
            /*Cria uma lista de números:
                5,8,12,3,7 
                Usa First para encontrar o primeiro número maior que 6.*/
            /*List<int> numeros = new List<int> { 5, 8, 12, 3, 7 };
            var primOcorr = numeros.First(n=> n%2 == 0);
            Console.WriteLine(primOcorr);*/
        }
    }
}
