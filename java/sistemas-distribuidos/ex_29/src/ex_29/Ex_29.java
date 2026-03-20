/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_29;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_29 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que pede um número e depois imprime por ordem 
        decrescente até chegar ao 1. */
        int i, num;
        num = Integer.parseInt(JOptionPane.showInputDialog(null, "Qual "
                + "o número?"));
        for (i=num; i>=1; i--){
            JOptionPane.showMessageDialog(null, i);
        }

    }
    
}
