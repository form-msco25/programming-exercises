"""Crie uma classe `Biblioteca` com o seguinte atributo:
- `livros` (lista de objetos Livro - reutilize a classe do Exercício 1)
Implemente os seguintes métodos:
- `adicionar_livro(livro)`: adiciona um livro à biblioteca
- `remover_livro(titulo)`: remove um livro pelo título
- `buscar_livro(titulo)`: retorna o livro se encontrado, None caso contrário
- `listar_todos()`: imprime todos os livros na biblioteca
- `contar_livros()`: retorna a quantidade de livros
**Teste:** Crie uma biblioteca, adicione 3 livros, busque um por título, remova um
e liste todos."""
class Livro:
        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor
        def __str__(self):
            return f"{self.titulo} - {self.autor}"
class Biblioteca:    
    def __init__(self):
        self.livros = []
    def adicionar_livro(self, livro):        
        self.livros.append(livro)
    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return
        print("Livro não encontrado.")
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro        
        return None
    def listar_todos(self):
        print("\nLivros na biblioteca:")
        for livro in self.livros:
            print("-", livro)
    def contar_livros(self):
        return len(self.livros)
    
biblio = Biblioteca()

livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("O Hobbit", "J. R. R. Tolkien")

biblio.adicionar_livro(livro1)
biblio.adicionar_livro(livro2)
biblio.adicionar_livro(livro3)

resultado = biblio.buscar_livro("1984")
if resultado:
    print("\nLivro encontrado:", resultado)

biblio.remover_livro("Dom Quixote")

biblio.listar_todos()
print("\nTotal de livros:", biblio.contar_livros())