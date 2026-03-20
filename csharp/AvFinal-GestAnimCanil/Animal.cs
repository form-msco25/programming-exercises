using System;
using System.Collections.Generic;
using System.Text;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace AvFinal_GestAnimCanil
{
    public class Animal
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string IdMongo { get; set; }
        public int id {  get; private set; }
        private string nome;
        private int idade;
        private decimal peso;

        public string Nome
        { 
            get { return nome; }
            set 
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("O nome não pode ser vazio.");
                nome = value; 
            }
        }
        public int Idade
        {
            get { return idade; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("A idade não pode ser inferior a 0.");
                idade = value;
            }
        }
        public decimal Peso
        {
            get { return peso; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("O peso não pode ser inferior a 0.");
                peso = value;
            }
        }
        public Animal(){}
        public Animal(int id, string nome, int idade, decimal peso)
        {
            this.id = id;
            Nome = nome;
            Idade = idade;
            Peso = peso;

        }        
        public Animal(string nome, int idade)
        {
            Nome = nome;
            Idade = idade;            
        }        

        public override string ToString()
        {
            return $"Id: {id} | Nome: {Nome} | Idade: {Idade} | Peso: {Peso}";
        }
    }
}
