/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_28;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_28 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que pede um número e depois imprime a tabuada do 
        número solicitado.*/
        int i, num;
        num = Integer.parseInt(JOptionPane.showInputDialog(null, "Qual "
                + "o número?"));
        String msg = "<html>TABUADA DO Nº" + num + "<br>";
        // Sintaxe do ciclo for (início; condição_paragem; passo)
        for(i=1; i<=10; i++){
            int prod = (num*i);
            JOptionPane.showMessageDialog(null, prod);
            // msg = msg+ "";
        }
    }
    
}
