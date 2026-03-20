/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_20;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Conversor temperaturas
 */
public class Ex_20 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Descreva um programa que a partir de uma temperatura expressa em 
        graus Fahrenheit (tempF), calcule a temperatura expressa em 
        graus Celsius (tempC). F = 32 +((9*C)/5); C = 5/9 x (F – 32)*/
        float f = Float.parseFloat(JOptionPane.showInputDialog("Digite a "
                + "temperatura em graus Fahrenheit:"));
        float c = (5f/9f) * (f - 32);
        JOptionPane.showMessageDialog(null, "Temperatura em graus Celsius = " 
                + c);
        
    }
    
}
