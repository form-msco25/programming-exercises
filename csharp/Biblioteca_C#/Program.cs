namespace Biblioteca_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // instanciar objetos
            Livro livro1 = new Livro("Os Maias", "Eça de Queirós", 1888);
            Livro livro2 = new Livro("1984", "George Orwell", 1949);
            Revista revista1 = new Revista("National Geographic", "Vários", 2024, 10);            
            Leitor leitor1 = new Leitor("Michael Ortiz", 1);
            Biblioteca biblioteca1 = new Biblioteca("Biblioteca Municipal Cataño");
            // adicionar
            biblioteca1.AdicionarLivro(livro1);
            biblioteca1.AdicionarLivro(livro2);
            biblioteca1.AdicionarLivro(revista1);
            // empréstimos
            leitor1.RequisitarLivro(livro1);
            leitor1.RequisitarLivro(livro2);
            leitor1.RequisitarLivro(revista1);
            // inserir funcionários
            biblioteca1.InputFuncionarios();
            // print informação
            Console.WriteLine("\n----- ESTADO DO LEITOR -----");
            Console.WriteLine(leitor1);
            Console.WriteLine("\n----- LIVROS DA BIBLIOTECA -----");
            biblioteca1.ListarLivros();
            Console.WriteLine("\n----- FUNCIONÁRIOS -----");
            biblioteca1.ListarFuncionarios();
        }
    }
}
