namespace Stand
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Carro carro1 = new Carro("Ford", "Fiesta", "XX-24-81", 2000, "Diesel");
            Carro carro2 = new Carro("Honda", "Civic", 2012, "Gasolina");
            Console.WriteLine(carro1);
            Console.WriteLine(carro2);
            carro1.Ligar();

            Carrinha carrinha1 = new Carrinha("Volvo", "V60", "99-XX-99", 2016, "Híbrido", 7);
            carrinha1.Ligar();
            Console.WriteLine(carrinha1);

            Stand stand1 = new Stand("Camões", "Rua dos Camões");
            stand1.AdicionarCarro(carro1);
            stand1.AdicionarCarro(carro2);

            /* Criar e inicializar lista de Carros
            List<Carro> listaCarros = new List<Carro>();
            listaCarros.Add(carro1);
            listaCarros.Add(carro2);

            foreach (Carro carro in listaCarros)
            {
                Console.WriteLine(carro);
            } */

            stand1.InputVendedor();
        }
    }
}