using System.Collections;
using System.Runtime.Intrinsics.X86;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Nivel4_Listas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* 13. Lista de nomes
               * Lê 5 nomes e guarda numa lista.
               * Mostra todos os nomes usando foreach.*/
            /* List<string> nomes = new List<string>();
            for (int i = 0; i < 5; i++) 
            {
                Console.WriteLine("\nDigite um nome: ");
                nomes.Add(Console.ReadLine());
            }
            Console.WriteLine("\nLista de nomes: ");
            foreach (string nome in nomes) 
            {
                Console.Write(nome + "");
            }*/
            /* 14. Remover elementos da lista
                * Lê 5 números e guarda numa lista.
                * Remove todos os números pares e mostra a lista atualizada.*/
            /*
            List<int> numeros = new List<int>();
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("\nDigite um número: ");
                numeros.Add(int.Parse(Console.ReadLine()));
            }
            Console.WriteLine("\nLista de números: ");
            foreach (int num in numeros)
            {
                Console.Write(num + " ");
            }
            // Remove(valor)
            // RemoveAt(indice)
            // RemoveAll(condição)
            numeros.RemoveAll(num => num % 2 == 0);
            /* for (int i = 0; i < numeros.Count; i++)
            {
                if (numeros[i] % 2 == 0)
                {
                    numeros.Remove(numeros[i]);
                    i--; // em reversa por motivo de ir tirando elementos da lista e consequentemente o índice ir mudando
                }
            }*/
            /*Console.WriteLine("\nLista atualizada: ");
            foreach (int num in numeros)
            {
                Console.Write(num + " ");
            }
            */
            /* 15. Contar elementos repetidos
                *Lê uma lista de números e conta quantas vezes cada número aparece.*/
            /* List<int> numeros = new List<int>();
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("\nDigite um número: ");
                numeros.Add(int.Parse(Console.ReadLine()));
            }
            Console.WriteLine("\nDigite o número que deseja verificar: ");
            int ver = int.Parse(Console.ReadLine());
            int contador = 0;
            foreach (int num in numeros)
            {
                if (num == ver)
                {
                    contador++;
                }                
            }
            Console.WriteLine($"\nO número {ver} aparece {contador} vezes.");
            */

        }
    }
}
