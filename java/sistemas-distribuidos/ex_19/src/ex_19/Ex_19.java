/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_19;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Cálculo da hipotenusa
 */
public class Ex_19 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Escreva um algoritmo para determinar a hipotenusa de um 
        triângulo rectângulo, dados os catetos.
        Nota: h^2 = c1^2 + c2^2 */
        float c1 = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor do primeiro cateto"));
        float c2 = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor do segundo cateto"));
        float h = (float) Math.sqrt((c1*c1) + (c2*c2));
        JOptionPane.showMessageDialog(null, "Hipotenusa = " + h);
        
    }
    
}
