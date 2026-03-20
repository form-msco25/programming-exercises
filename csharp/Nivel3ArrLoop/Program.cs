using System.Security.Cryptography;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Nivel3ArrLoop
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* 9. Média de notas 
                 * Lê 5 notas e guarda num array. 
                 * Calcula e imprime a média usando for.*/
            /*int[] numeros = new int[5];
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Digite um número: ");
                int num = int.Parse(Console.ReadLine());
                numeros[i] = num;
            }
            int soma = 0;
            double media = 0;
            foreach (int num in numeros) 
            {
                soma += num;                
            }
            media = soma / numeros.Length;
            Console.WriteLine($"A média dos números no vetor é igual a {media}");*/
            /* 10.Maior e menor número 
                * Lê 10 números e guarda num array. 
                * Determina o maior e o menor usando for.*/
            /*int[] numeros = new int[10];            
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.WriteLine("Digite um número: ");
                int num = int.Parse(Console.ReadLine());
                numeros[i] = num;                
            }
            int maior = numeros[0];
            int menor = numeros[0];
            for (int i = 1; i < numeros.Length; i++)
            {
                if (numeros[i] > maior)
                {
                    maior = numeros[i];
                }

                if (numeros[i] < menor)
                {
                    menor = numeros[i];
                }
            }
            Console.WriteLine($"Número maior = {maior}");
            Console.WriteLine($"Número menor = {menor}");*/
            /* 11.Invertendo um array 
                Lê 5 números e mostra o array invertido.*/
            /* int[] numeros = new int[5];
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.WriteLine("\nDigite um valor do vetor: ");              
                numeros[i] = int.Parse(Console.ReadLine());
            }
            int[] numerosInvert = new int[numeros.Length];
            for (int i = 0; i < numeros.Length; i++)
            {
                numerosInvert[i] = numeros[numeros.Length - 1 - i];
            }
            Console.WriteLine($"\nVetor original: ");            
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.Write(numeros[i] + " ");
            }
            Console.WriteLine($"\nVetor invertido: ");
            for (int i = 0; i < numerosInvert.Length; i++)
            {
                Console.Write(numerosInvert[i] + " ");
            }*/
            /* 12.Soma de elementos de um array 
                Usa foreach para somar todos os elementos do array*/
            /*int[] elementos = { 1, 2, 3, 4, 5 };
            int soma = 0;
            foreach (int valor in elementos)
            {
                soma += valor;
            }
            Console.Write("\nVetor: ");
            for (int i = 0; i < elementos.Length; i++)
            {
                Console.Write(elementos[i] + " ");
            }
            Console.WriteLine($"\nSoma dos valores do vetor: {soma}");*/
        }
    }
}
