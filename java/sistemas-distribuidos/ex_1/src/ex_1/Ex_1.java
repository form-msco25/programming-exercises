/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_1;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author micha
 * Função: Exercícios iniciais
 */
public class Ex_1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // código deve ser colocado aqui
        // exercício 1 - exemplo de output
        System.out.println("Olá! Bem-vindo ao Java");
        // exercício 2 - concatenação de variáveis
        String cidade="Porto";
        System.out.println("Tu moras em " +cidade);
        // exercício 3 - operadores aritméticos
        int ano=1976;
        int idade;
        idade = 49;
        int ano_atual = ano+idade;
        System.out.println("Caso te tenhas esquecido estamos em " +ano_atual);
        JOptionPane.showMessageDialog(null, "<html>Olá! Moras no " +cidade +
                ", <br>Estamos no ano de " + ano_atual);
        // exercício 4 - somar 2 números
        String n1, n2;
        n1=JOptionPane.showInputDialog("Qual o número 1?");
        n2=JOptionPane.showInputDialog("Qual o número 2?");
        int soma = Integer.parseInt(n1)+Integer.parseInt(n2);
        JOptionPane.showMessageDialog(null, "A soma de " + n1 + " com " + n2 +
                " = " + soma);
    }
    
}
