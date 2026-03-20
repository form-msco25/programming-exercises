/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_16;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Operações aritméticas
 */
public class Ex_16 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador dois números. O programa 
        deve mostrar a soma, a multiplicação, a divisão e a subtracção. */
        double n1 = Double.parseDouble(JOptionPane.showInputDialog(null, "Insira o primeiro número:"));
        double n2 = Double.parseDouble(JOptionPane.showInputDialog(null, "Insira o segundo número:"));
        
        double soma = n1 + n2;
        JOptionPane.showMessageDialog(null, "A soma dos valores é " + soma);
        double sub = n1 - n2;
        JOptionPane.showMessageDialog(null, "A subtracção dos valores é " + sub);
        double mul = n1 * n2;
        JOptionPane.showMessageDialog(null, "A multiplicação dos valores é " + mul);
        double div = n1 / n2;
        if (n2 != 0)
            JOptionPane.showMessageDialog(null, "A divisão dos valores é " + div);
        else
            JOptionPane.showMessageDialog(null, "O segundo valor inserido é inválido");
        
    }
    
}
