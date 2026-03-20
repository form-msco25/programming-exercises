using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using MVC_Viatura.Models;

namespace MVC_Viatura.Data
{
    public class MVC_ViaturaContext : DbContext
    {
        public MVC_ViaturaContext (DbContextOptions<MVC_ViaturaContext> options)
            : base(options)
        {
        }

        public DbSet<MVC_Viatura.Models.Vendedor> Vendedor { get; set; } = default!;
        public DbSet<MVC_Viatura.Models.Viatura> Viatura { get; set; } = default!;
        public DbSet<MVC_Viatura.Models.Cliente> Cliente { get; set; } = default!;
    }
}
