using Microsoft.VisualBasic;

namespace Parte1_Strings_Basic_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ex1.Cria duas variáveis string com o teu nome e apelido.
            //    Concatena as duas strings e mostra o resultado no ecrã.
            /*string nome = "Michael";
            string apelido = "Ortiz";
            Console.WriteLine(nome + " " + apelido);*/
            //Ex2.Cria uma string com a frase: Aprender C# é divertido
            //    Usa Substring para extrair apenas a palavra Aprender.
            /*string frase = "Aprender C# é divertido.";
            string sub = frase.Substring(0, 8);
            Console.WriteLine(sub);*/
            //Ex3.Cria a string: Eu gosto de programação
            //    Utiliza Replace para substituir programação por C#.
            /*string frase = "Eu gosto de programação.";            
            Console.WriteLine(frase.Replace("programação", "C#"));*/
            //Ex4.Cria uma string com a frase: C# é uma linguagem poderosa
            //    Usa IndexOf para descobrir a posição da palavra 'linguagem'.
            /*string frase = "C# é uma linguagem poderosa.";
            Console.WriteLine($"Índice da palavra 'linguagem': {frase.IndexOf("linguagem")}");*/
            //Ex5.Pede ao utilizador uma frase. Mostra: 
            //    A frase original, A posição da primeira letra a usando IndexOf
            /*Console.Write("Insira uma frase: ");
            string frase = Console.ReadLine();
            Console.WriteLine($"Frase digitada: {frase}");
            Console.WriteLine($"Posição da primeira letra 'a': {frase.IndexOf('a') + 1}");*/
        }
    }
}
