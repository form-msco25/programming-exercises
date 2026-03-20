using System;
using System.Collections.Generic;
using System.Text;

namespace Stand
{
    public class Carro
    {
        // 1. Propriedades ou campos da classe
        public string marca;
        public string modelo;
        public string matricula;
        public int anoMatricula;
        public string combustivel;
        public float preco;
        // 2. Construtor
        public Carro(string marca, string modelo, string matricula, int anoMatricula, string combustivel, float preco)
        {
            this.marca = marca;
            this.modelo = modelo;
            this.matricula = matricula;
            this.anoMatricula = anoMatricula;
            this.combustivel = combustivel;
            this.preco = preco;
        }
        public Carro(string marca, string modelo, string matricula, int anoMatricula, string combustivel)
        {
            this.marca = marca;
            this.modelo = modelo;
            this.matricula = matricula;
            this.anoMatricula = anoMatricula;
            this.combustivel = combustivel;
            this.preco = 0.0f;
        }
        // 3. Polimorfismo: dois contrutores com parámetros diferentes
        public Carro(string marca, string modelo, int anoMatricula, string combustivel)
        {
            this.marca = marca;
            this.modelo = modelo;
            this.matricula = "indefinida";
            this.anoMatricula = anoMatricula;
            this.combustivel = combustivel;
        }
        public void Ligar()
        {
            Console.WriteLine("\nVRuumTatatá");
        }
        // Vamos dar override à função 'toString' para poder imprimir corretamente todos os campos da classe
        public override string ToString()
        {
            return $"\nMarca: {marca} | Modelo: {modelo} | Matrícula: {matricula} | Ano: {anoMatricula} | Combustível: {combustivel}";
        }
    }
}