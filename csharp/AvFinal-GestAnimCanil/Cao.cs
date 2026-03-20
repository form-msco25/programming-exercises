using System;
using System.Collections.Generic;
using System.Text;

namespace AvFinal_GestAnimCanil
{
    public class Cao : Animal
    {
        private string raca;
        private string porte;

        public string Raca
        {
            get { return raca; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("A raça não pode ser vazia.");
                raca = value;
            }
        }
        public string Porte
        {
            get { return porte; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("O porte não pode ser vazio.");
                porte = value;
            }
        }

        public Cao() : base(){}

        public Cao(int id, string nome, int idade, decimal peso, string raca, string porte): base(id, nome, idade, peso) 
        {   
            Raca = raca;
            Porte = porte; 
        }

        public Cao(int id, string nome, int idade, decimal peso, string raca) : base(id, nome, idade, peso)
        {
            Raca = raca;
            Porte = "Indefinido";
        }

        public override string ToString()
        {
            return base.ToString() + $"Raça: {Raca} | Porte: {Porte}";
        }
    }
}
