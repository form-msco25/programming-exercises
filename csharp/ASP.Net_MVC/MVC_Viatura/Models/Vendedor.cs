using System.ComponentModel.DataAnnotations;

namespace MVC_Viatura.Models
{
    public class Vendedor
    {
        public int Id { get; set; }

        [Display(Name = "Nome")]
        public string? Nome { get; set; }        

        [Display(Name = "Morada")]
        public string? Morada { get; set; }

        [Display(Name = "E-mail")]
        public string? Email { get; set; }

        [Display(Name = "Telefone")]
        public int Telefone { get; set; }

        [Display(Name = "NIB")]
        public int Nib { get; set; }

        [Display(Name = "NIF")]
        public int Contribuinte { get; set; }
    }
}
