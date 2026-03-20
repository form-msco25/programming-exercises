using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Website_Pessoal.Models;

namespace Website_Pessoal.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }
        public IActionResult SobreMim()
        {
            return View();
        }
        public IActionResult Formacao()
        {
            return View();
        }
        public IActionResult Interesses()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}