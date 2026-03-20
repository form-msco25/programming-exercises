/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_11;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Exercícios de reforço
 */
public class Ex_11 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador o valor do raio. 
        O programa deve mostrar a área e o perímetro. */
        double raio = Double.parseDouble(JOptionPane.showInputDialog(null,
                "Insira o raio do círculo ou circumferência"));
        double area = raio*raio * Math.PI;
        double perimetro = Math.PI * (raio*2);
        JOptionPane.showMessageDialog(null, "<html> Área = " + area + 
                "<br> Perímetro = " + perimetro);
    }    
}
