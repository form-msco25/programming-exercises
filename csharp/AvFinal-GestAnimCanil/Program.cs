using MongoDB.Driver;
namespace AvFinal_GestAnimCanil
{
    internal class Program
    {
        static List<Cao> animais = new List<Cao>();
        static string[] racas = { "French Bulldog", "Beagle", "Serra da Estrela" };
        static string[] portes = { "Pequeno", "Médio", "Grande" };
        static MongoDB mongo = new MongoDB();
        static int proximoId = 1;
        static void Main(string[] args)
        {
            int opcao;
            do
            {
                Console.WriteLine("\nDigite um número: \n\n1-Adicionar\n2-Listar\n3-Procurar\n4-Remover" + 
                    "\n5-Guardar no MongoDB\n6-Ler do MongoDB\n0-Sair");
                if (!int.TryParse(Console.ReadLine(), out opcao))
                {
                    Console.WriteLine("Escolha inválida!");
                    continue;
                }
                switch (opcao)
                {
                    case 1: AdicionarAnimal(); break;
                    case 2: ListarAnimais(); break;
                    case 3: ProcurarAnimal(); break;
                    case 4: RemoverAnimal(); break;
                    case 5:
                        mongo.Guardar(animais);
                        Console.WriteLine("Animais guardados no MongoDB!");
                        break;
                    case 6:
                        animais = mongo.Ler();
                        Console.WriteLine("Animais carregados do MongoDB!");
                        ListarAnimais();
                        break;
                    case 0: break;
                    default: Console.WriteLine("Opção inválida!"); break;
                }
            } while (opcao != 0);
        }
        static void AdicionarAnimal()
        {
            int id = proximoId++;

            Console.Write("Nome: ");
            string nome = Console.ReadLine();

            Console.Write("Idade: ");
            int idade = int.Parse(Console.ReadLine());

            Console.Write("Peso: ");
            decimal peso = decimal.Parse(Console.ReadLine());

            Console.WriteLine("Raças disponíveis:");
            foreach (var r in racas)
                Console.WriteLine(r);
            Console.Write("Raça: ");
            string raca = Console.ReadLine();

            Console.WriteLine("Portes disponíveis:");
            foreach (var p in portes)
                Console.WriteLine(p);
            Console.Write("Porte: ");
            string porte = Console.ReadLine();

            Cao cao = new Cao(id, nome, idade, peso, raca, porte);

            animais.Add(cao);
        }
        static void ListarAnimais()
        {
            if (!animais.Any())
            {
                Console.WriteLine("Não existem animais.");
                return;
            }
            foreach (var animal in animais)
            {
                Console.WriteLine("\n" + animal);
            }
        }
        static void ProcurarAnimal()
        {
            Console.Write("Nome: ");
            string nome = Console.ReadLine();
            var encontrados = animais.Where(a => a.Nome.ToLower() == nome.ToLower());
            if (!encontrados.Any())
            {
                Console.WriteLine("Nenhum animal encontrado.");
                return;
            }
            foreach (var animal in encontrados)
            {
                Console.WriteLine(animal);
            }
        }
        static void RemoverAnimal()
        {
            Console.Write("Id: ");
            int id = int.Parse(Console.ReadLine());
            var animal = animais.FirstOrDefault(a => a.id == id);
            if (animal != null)
            {
                animais.Remove(animal);
                Console.WriteLine("Removido!");
            }
            else
            {
                Console.WriteLine("Não encontrado.");
            }
        }
    }
}