/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_34;

import javax.swing.JOptionPane;

/**
 * Data: 17/11/2025
 * @author michael
 */
public class Ex_34 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /*Faça um programa que lê 5 idades e depois imprime a média 
        dessas idades.*/
        int idade[]= new int[5];        
        int soma = 0;
        int i;
        
        for (i=0; i<5; i++){
            idade[i]=Integer.parseInt(JOptionPane.showInputDialog("Insira as "
                    + "idades: "));            
        }
        for (i=0; i<5; i++){
            soma = soma + idade[i];        
        }
        float media = soma / 5f;        
        JOptionPane.showMessageDialog(null,"A idade média é: " + media);
    
    }
    
}
