/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_15;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Converter unidades de medidas
 */
public class Ex_15 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador o valor em polegadas 
        e depois converte para centímetros.
        Considere que 1 polegada são 2,54 centímetros. */
        String val1 = JOptionPane.showInputDialog(null, "Digite o valor "
                + "em polegadas:");
        double val2 = Double.parseDouble(val1) * 2.54;
        JOptionPane.showMessageDialog(null, val1 + " polegadas = " + val2 + 
                " centímetros.");
        
    }
    
}
