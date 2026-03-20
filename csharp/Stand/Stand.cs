using System;
using System.Collections.Generic;
using System.Text;

namespace Stand
{
    public class Stand
    {
        public string nome;
        public string morada;
        private List<Carro> listaCarros;
        public string[] vendedores;
        // Construtor
        public Stand(string nome, string morada)
        {
            this.nome = nome;
            this.morada = morada;
            listaCarros = new List<Carro>();
            vendedores = new string[5];
        }
        // função 'private' por que só é utilizada nesta classe
        private void AdicionarVendedor(int pos, string nome)
        {
            vendedores[pos] = nome;
        }
        public void InputVendedor()
        {
            for (int i = 0; i < vendedores.Length; i++)
            {
                Console.WriteLine("\nInsira o nome do vendedor: " + (i+1));
                string nome = Console.ReadLine();
                AdicionarVendedor(i, nome);
            }
        }
        public void AdicionarCarro(Carro carro)
        {
            if (carro == null)
            {
                Console.WriteLine("Inválido.Carro Nulo.");
            }
            else
            {
                listaCarros.Add(carro);
            }
        }
    }
}