using System.ComponentModel.DataAnnotations;

namespace MVC_Viatura.Models
{
    public class Cliente
    {
        public int Id { get; set; }
        public string? Nome { get; set; }
        public string? Morada { get; set; }

        [Display(Name = "Data de Nascimento")]
        [DataType(DataType.Date)]
        public DateTime DataNasc { get; set; }

        [Display(Name = "E-mail")]
        public string? Email { get; set; }

        public int Telefone { get; set; }
    }
}
