namespace Nivel1_CondSimp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* 1. Número positivo, negativo ou zero 
               * Lê um número do utilizador e mostra se é positivo, negativo ou zero.*/
            /*Console.WriteLine("Digite um número: ");
            string entrada = Console.ReadLine();
            int num = int.Parse(entrada);            
            if (num > 0)
            {
                Console.WriteLine("\nO número que digitou é positivo.");
            }
            else if (num < 0)
            {
                Console.WriteLine("O número que digitou é negativo.");
            }
            else
            {
                Console.WriteLine("O número que digitou é igual a zero.");
            }*/
            /////////////////////////
            /* 2. Maior de três números 
                * Lê três números e mostra qual é o maior usando if / else if / else.*/
            /*Console.WriteLine("\nDigite o primeiro número: ");
            int n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("\nDigite o segundo número: ");
            int n2 = int.Parse(Console.ReadLine());
            Console.WriteLine("\nDigite o terceiro número: ");
            int n3 = int.Parse(Console.ReadLine());
            int maior;
            if (n1 > n2 && n1>n3)
            {
                maior = n1;                
            }
            else if (n2 > n1 && n2 > n3)
            {
                maior = n2;
            }
            else
            {
                maior = n3;
            }
            Console.WriteLine($"\nO número maior é igual a {maior}");*/
            /* 3. Par ou ímpar 
               * Lê um número e indica se é par ou ímpar.*/
            Console.WriteLine("\nDigite o número: ");
            int num = int.Parse(Console.ReadLine());
            if (num == 0)
            {
                Console.WriteLine("O número é igual a zero.");
            }
            else if (num % 2 == 0)
            {
                Console.WriteLine("O número é par.");
            }
            else
            {
                Console.WriteLine("O número é ímpar");
            }
        }
    }
}