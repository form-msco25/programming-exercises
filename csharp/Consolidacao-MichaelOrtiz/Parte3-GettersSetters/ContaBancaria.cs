using System;
using System.Collections.Generic;
using System.Text;

namespace Parte3_GettersSetters
{
    public class ContaBancaria
    {
        //Ex.12
        /*Cria uma classe ContaBancaria com:
            Titular
            Saldo
            Permite ler o saldo(get) mas apenas a própria classe pode modificar o saldo(private set).*/
        public string Titular { get; set; }
        public decimal Saldo { get; private set; }
        public void Depositar(decimal valor)
        {
            Saldo += valor;
        }
    }
}
