/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_35;

import javax.swing.JOptionPane;

/**
 * Data: 17/11/2025
 * @author michael
 */
public class Ex_35 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que lê 8 pesos (valor decimal) e depois as imprime, 
        bem como a média.*/
        int tam = 8;
        float peso[] = new float[tam];
        float soma = 0;
        for (int i=0; i<8; i++){
            peso[i]=Float.parseFloat(JOptionPane.showInputDialog("Insira "
                    + "o peso: "));            
        }
        for (int i=0; i<8; i++){
            soma = soma + peso[i];
        }
        float media = soma / 8f;
        JOptionPane.showMessageDialog(null, "A média dos pesos é " + media);
        
        
    }
    
}
