using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace MVC_Livro.Models
{
    public class Livro
    {
        public int Id { get; set; }
     
        [Display(Name = "Título")]
        public string? Titulo { get; set; } // '? define o tamanho como máximo no array de caracteres

        [Display(Name = "Data de Lançamento")]
        [DataType(DataType.Date)]        
        public DateTime DataLancamento { get; set; }

        [Display(Name = "Género")]
        public string? Genero { get; set; }

        [Display(Name = "Preço")]
        [Column(TypeName = "decimal(8,2)")]
        public decimal Preco { get; set; }
    }
}
