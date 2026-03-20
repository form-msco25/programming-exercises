using System.Runtime.Intrinsics.X86;
using System.Text;

namespace Parte2_StringBuilder
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Ex6.Utiliza StringBuilder para criar uma string com os números de 1 a 5 separados por vírgula.
            /*StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 5; i++)
            {
                if (i == 4)
                {
                    sb.Append(i+1);
                }
                else
                {
                    sb.Append((i + 1) + ",");
                }                
            }
            Console.WriteLine(sb.ToString());*/
            //Ex7.Usa StringBuilder para construir a frase: 
            //    Hoje estou a aprender C#.
            //    Adiciona cada palavra com Append.
            /*StringBuilder sb = new StringBuilder();
            sb.Append("Hoje ");
            sb.Append("estou ");
            sb.Append("a ");
            sb.Append("aprender ");
            sb.Append("C#.");
            Console.WriteLine(sb.ToString());*/
            //Ex8.Utiliza StringBuilder dentro de um loop para criar uma sequência de números de 1 a 20 separados por espaço.
            /*StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 20; i++)
            {   if (i==19)
                {
                    sb.Append(i + 1);
                }
                else
                {
                    sb.Append((i + 1) + " ");
                }               
            }
            Console.WriteLine(sb.ToString());*/
        }
    }
}
