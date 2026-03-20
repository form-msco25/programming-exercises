/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_23;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Classificação triángulo
 */
public class Ex_23 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Classificar um triângulo quanto aos lados, sendo que um triângulo 
        com todos lados iguais é designado Equilátero, com todos os lados diferentes 
        entre si é designado Escaleno e caso tenha apenas dois lados iguais entre si, 
        designa-se Isósceles. */
        float lado1 = Float.parseFloat(JOptionPane.showInputDialog("Insira um "
                + "dos lados do triângulo: "));
        float lado2 = Float.parseFloat(JOptionPane.showInputDialog("Insira "
                + "outro lado do triângulo: "));
        float lado3 = Float.parseFloat(JOptionPane.showInputDialog("Insira o "
                + "último lado do triângulo: "));
        
        if (lado1 == lado2 && lado2 == lado3){
            JOptionPane.showMessageDialog(null, "Equilátero");
        }
        else if (lado1 != lado2 && lado2 != lado3 && lado1 != lado3){
                JOptionPane.showMessageDialog(null, "Escaleno");
            }
        else{
            JOptionPane.showMessageDialog(null, "Isósceles");
        }
        
    }
    
}
