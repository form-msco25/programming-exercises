using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using MVC_Livro.Models;

namespace MVC_Livro.Data
{
    public class MVC_LivroContext : DbContext
    {
        public MVC_LivroContext (DbContextOptions<MVC_LivroContext> options)
            : base(options)
        {
        }

        public DbSet<MVC_Livro.Models.Livro> Livro { get; set; } = default!;
    }
}
