/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_10;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Exercícios de reforço
 */
public class Ex_10 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador os valores de dois lados 
        diferentes de um rectângulo. O programa deve mostrar a área 
        e o perímetro.*/
        String lado1, lado2;        
        lado1=JOptionPane.showInputDialog(null,"Insira um lado do rectángulo");
        lado2=JOptionPane.showInputDialog(null,"Insira um lado diferente "
                + "do rectángulo:");
        float area = (Float.parseFloat(lado1)) 
                * (Float.parseFloat(lado2));
        float perimetro = (Float.parseFloat(lado1) 
                + Float.parseFloat(lado2)) * 2;
        JOptionPane.showMessageDialog(null, "<html> Área = " + area 
                + "<br> Perímetro = " + perimetro);
    }
    
}
