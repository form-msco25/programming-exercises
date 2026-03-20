/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_30;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_30 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que tem o seguinte output:
        Quantos números deseja? 6
        Indique o valor inicial? 20
        
        Listagem de números:
        20-21-22-23-24-25-26
        */
        int num, valor_inicial, i;
        num = Integer.parseInt(JOptionPane.showInputDialog("Quantos números "
                + "deseja?"));
        valor_inicial = Integer.parseInt(JOptionPane.showInputDialog("Indique "
                + "o valor inicial: "));
        for (i=0; i<=num; i++){
            JOptionPane.showMessageDialog(null,valor_inicial);
            valor_inicial = valor_inicial + 1;
        }

    }
    
}
