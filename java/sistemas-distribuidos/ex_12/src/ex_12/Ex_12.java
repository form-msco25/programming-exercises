/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_12;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Uso da consola (terminal)
 */
public class Ex_12 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int var1; // assim se declara a variavel var1 como inteiro.
        double var2; //assim se declara a variavel var2 como floating point
        var1 = 10; //atribui o valor inicial a var1
        var2 = 10.0; //atribui o valor inicial a var2 (com decimais)
        System.out.println ("Valor inicial de var1: " + var1);
        System.out.println ("Valor inicial de var2: " + var2);
        System.out.println (); //imprime uma linha em branco

       // vamos dividir ambas as variavéis por 4

        var1 = var1 / 4; //vai truncar o resultado
        var2 = var2 / 4; //vai dar o resultado completo

        System.out.println("Valor após a divisão por 4 - var1: " + var1);
        System.out.println("Valor após a divisão por 4 - var2: " + var2);

    }
    
}
