"""Crie uma classe `Animal` com os seguintes atributos:
- `nome` (string)
- `especie` (string)
Implemente um método `fazer_som()` que imprime "Som genérico do animal".
Crie uma subclasse `Cachorro` que herda de `Animal` e sobrescreve o método
`fazer_som()` para imprimir "Au au!".
Crie uma subclasse `Gato` que herda de `Animal` e sobrescreve o método
`fazer_som()` para imprimir "Miau!".
**Teste:** Crie um Cachorro e um Gato, e chame o método `fazer_som()` para
cada um."""
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    def fazer_som(self):
        print("Som genérico do animal")
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

cao = Cachorro("Zeus", "Cão")
gato = Gato("Fosca", "Gato")

cao.fazer_som()
gato.fazer_som()