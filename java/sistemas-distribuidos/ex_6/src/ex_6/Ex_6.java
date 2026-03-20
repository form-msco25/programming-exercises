/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_6;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author micha
 * Função: Exercícios iniciais
 */
public class Ex_6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        // exercício 6 - temperaturas
        String t1, t2, t3;
        t1=JOptionPane.showInputDialog("Digite a primeira temperatura: ");
        t2=JOptionPane.showInputDialog("Digite a segunda temperatura: ");
        t3=JOptionPane.showInputDialog("Digite a terceira temperatura: ");
        float media = Float.parseFloat(t1) + Float.parseFloat(t2) + 
                Float.parseFloat(t3) / 3;        
        JOptionPane.showMessageDialog(null, "A média das 3 temperaturas = "
                + media);
    }
    
}
