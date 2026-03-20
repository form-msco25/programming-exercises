using System;
using System.Collections.Generic;
using System.Runtime.ConstrainedExecution;
using System.Text;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Parte3_GettersSetters
{
    public class Aluno
    {
        /*Cria uma classe Aluno com a propriedade:
            Nota
            No set, garante que a nota não pode ser negativa.
            Se for negativa, mostra uma mensagem de erro.*/
        private decimal nota;

        public decimal Nota
        {
            get { return nota; } 
            set
            {
                if (value >= 0)
                {
                    nota = value;
                }
                else
                {
                    throw new ArgumentException("A nota não pode ser negativa");
                }
            }
        }
    }
}
