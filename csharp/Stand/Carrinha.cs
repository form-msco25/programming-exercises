using System;
using System.Collections.Generic;
using System.Text;

namespace Stand
{
    // herança: classe 'carrinha' herda propriedades da classe 'carro',
    // juntamente com acesso às suas funções
    public class Carrinha : Carro
    {
        public int capacidade;

        public Carrinha(string marca, string modelo, string matricula, int anoMatricula, string combustivel, int capacidade) : 
            base(marca, modelo, matricula, anoMatricula, combustivel)
            //atributos respetivos de um dos construtores da classe carro
        {
            this.capacidade = capacidade;
        }
        public void Ligar()
        {
            Console.WriteLine("\nVRuumTatatá>>Carrinha");
        }
        public override string ToString()
        {
            return $"\nMarca: {marca} | Modelo: {modelo} | Matrícula: {matricula} " +
                $"| Ano: {anoMatricula} | Combustível: {combustivel} | Capacidade: {capacidade}";
        }
    }
}
