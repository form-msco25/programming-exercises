using static System.Net.Mime.MediaTypeNames;

namespace Nivel2_CicSimp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*4. Tabuada do número 
                * Lê um número e imprime a tabuada de 1 a 10 usando for.*/
            /*Console.WriteLine("Digite um número: ");
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine($"\nTabuada do {num}.\n");
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine($"{num} x {i} = {num * i}");
            }*/
            /////////////////////////
            /*5. Soma de números até zero 
                * O utilizador insere números até digitar 0. 
                * Soma todos os números inseridos (usar while ou do while).*/
            /*int soma = 0;
            bool cond = true;
            while (cond)
            {
                Console.WriteLine("Digite um número: ");
                int num = int.Parse(Console.ReadLine());                
                if (num == 0)
                {
                    Console.WriteLine("Número inserido: 0");
                    Console.WriteLine($"\nSoma dos números inseridos: {soma}");
                    Console.WriteLine("\nFim do programa.");
                    cond = false;
                }
                else
                {
                    soma += num;
                    Console.WriteLine($"Soma dos números inseridos: {soma}");      
                }

            }*/
            /*int num;
            int soma = 0;
            do
            {
                Console.WriteLine("\nDigite um número: ");
                num = int.Parse(Console.ReadLine());
                soma += num;
                Console.WriteLine($"\nSoma dos números inseridos: {soma}");
            }
            while (num != 0);            
            Console.WriteLine("\nNúmero inserido: 0");            
            Console.WriteLine("Fim do programa.");*/
            /////////////////////////
            /* 6. Contagem regressiva
                 * Lê um número e imprime a contagem regressiva até 0 usando for.*/
            /*Console.WriteLine("Digite um número: ");
            int num = int.Parse(Console.ReadLine());
            num -= 1;
            for (int i = num; i >= 0; i--)
            {
                Console.WriteLine(i);
            }*/
            /* 7. Números pares de 1 a 50 
                 * Imprime todos os números pares entre 1 e 50 usando for ou while.*/
            /*for (int i = 1; i <= 50; i++)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine(i);
                }
            }*/
            /*int num = 1;
            while (num <= 50)
            {
                if (num % 2 == 0)
                {
                    Console.WriteLine(num);
                }
                num++;
            }*/
            /////////////////////////
            /* 8. Número de tentativas até acertar 
                 * Gera um número aleatório entre 1 e 20. 
                 * O utilizador tenta adivinhar até acertar usando do while.*/
            /*Random random = new Random();
            int numRandom = random.Next(1, 21);
            int num;
            int tentativas = 0;
            do
            {
                Console.WriteLine("Digite um número e tente acertar o número aleatório: ");
                num = int.Parse(Console.ReadLine());
                tentativas ++;
            }
            while (num != numRandom);
            Console.WriteLine($"PARABÉNS!!! Acertou!\nO número aleatório era: {numRandom}");
            Console.WriteLine($"Número de tentativas: {tentativas}");*/
        }
    }
}
