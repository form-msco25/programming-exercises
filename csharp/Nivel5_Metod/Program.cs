using System.Runtime.Intrinsics.X86;

namespace Nivel5_Metod
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* 16. Função void - saudação
                * Cria uma função void que recebe o nome do utilizador e imprime: "Olá, [nome]!".*/
            /* void Saudacao(string nome)
            {
                Console.WriteLine($"\nOlá, {nome}!" );
            }
            Console.Write("\nDigite o seu nome: ");
            string nome = Console.ReadLine();
            Saudacao(nome);*/
            /* 17. Função com retorno - quadrado
                * Cria uma função que recebe um número e devolve o seu quadrado.*/
            /* int Quadrado(int num)
            {
                return num * num;
            }*/
            /* Console.Write("\nDigite um número: ");
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine($"\n{num} ao quadrado é igual a {Quadrado(num)}");*/
            /* Console.Write("\nDigite um número: ");
            if (int.TryParse(Console.ReadLine(), out int num))
            {
                Console.WriteLine($"\n{num} ao quadrado é igual a {Quadrado(num)}");
            }
            else
            {
                Console.WriteLine("Valor inválido.");
            }*/
            /* 18. Função para calcular média
                * Recebe um array de números e devolve a média(tipo double).*/
            /* double Media(int[] numeros)
            {
                int soma = 0;
                foreach (int num in numeros)
                {
                    soma += num;
                }
                return (double) soma / numeros.Length;
            }
            Console.Write("Digite o tamanho do vetor de números: ");
            int tam = int.Parse(Console.ReadLine());
            int[] numeros = new int[tam];
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.Write("Digite um número para o vetor 'números': ");
                numeros[i] = int.Parse(Console.ReadLine());
            }            
            Console.WriteLine($"A média dos valores do vetor 'números' é igual a {Media(numeros)}");*/
            /* 19.Função para verificar número par
                *Recebe um número e devolve true se for par, false caso contrário.*/
            /* bool NumPar(int num)
            {
                return num % 2 == 0;                
            }
            Console.Write("Digite um número: ");
            if (int.TryParse(Console.ReadLine(), out int numero))
            {
                if (NumPar(numero))
                    Console.WriteLine("\nO número é par");
                else
                    Console.WriteLine("\nO número não é par");
            }
            else
            {
                Console.WriteLine("Valor inválido.");
            }*/
            /* 20. Função para verificar número primo
                *Recebe um número e devolve true se for primo, false caso contrário.*/
            /* bool NumPrim(int num)
            {
                if (num <= 1)
                    return false;
                if (num == 2)
                    return true;
                if (num % 2 == 0)
                    return false;
                for (int i = 3; i <= Math.Sqrt(num); i += 2)
                {
                    if (num % i == 0)
                        return false;
                }
                return true;
            }
            Console.Write("\nDigite um número: ");
            if (NumPrim(int.Parse(Console.ReadLine())))
            {
                Console.WriteLine($"\nO número é primo.");
            }
            else
            {
                Console.WriteLine($"\nO número não é primo.");
            }*/
            /* 21. Função para inverter uma string
                * Recebe uma string e devolve a string invertida.*/
            /*string InverterString (string palavra)
            {
                char[] caracteres = palavra.ToCharArray(); // string para vetor de caracteres
                Array.Reverse(caracteres); // inverte o vetor
                return new string(caracteres); // cria string com caracteres invertidos
            }
            Console.Write("\nDigite uma palavra: ");            ;
            Console.WriteLine($"\nString invertida: {InverterString(Console.ReadLine())}");*/
            /* 22. Função para contar vogais
                * Recebe uma string e devolve o número de vogais que contém.*/
            /* int ContVogais(string palavra)
            {
                char[] caracteres = palavra.ToLower().ToCharArray();
                int vogais = 0;
                foreach (char c in caracteres)
                {
                    if (c == 'a') // aspas simples porque é char
                    {
                        vogais++;
                    }
                    else if (c == 'e')
                    {
                        vogais++;
                    }
                    else if (c == 'i')
                    {
                        vogais++;
                    }
                    else if (c == 'o')
                    {
                        vogais++;
                    }
                    else if (c == 'u')
                    {
                        vogais++;
                    }                    
                }
                return vogais;
            }
            Console.Write("Digite uma palavra: ");
            string palavra = Console.ReadLine();
            int resultado = ContVogais(palavra);
            if (resultado == 0)
                Console.WriteLine("A palavra não tem vogais.");
            else
                Console.WriteLine($"O número de vogais que contém a palavra '{palavra}' é: {resultado}");*/
            /* 23. Função de soma de dois números
                * Recebe dois números e devolve a soma.*/
            /* int Soma(int a, int b)
            {
                return a + b;
            }
            Console.Write("Digite o primeiro número: ");
            int a = int.Parse(Console.ReadLine());
            Console.Write("Digite o segundo número: ");
            int b = int.Parse(Console.ReadLine());
            Console.WriteLine($"A soma dos números é igual a {Soma(a, b)}");*/
            /* 24. Função void - imprimir números de 1 até N
                *Recebe um número N e imprime todos os números de 1 até N.*/
            /* void Print(int n)
            {
                for (int i = 1; i <= n; i++)
                {
                    Console.Write(i + " ");
                }
            }
            Console.Write("Digite um número: ");
            Print(int.Parse(Console.ReadLine()));*/
        }
    }
}
