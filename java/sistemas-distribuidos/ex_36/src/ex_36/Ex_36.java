/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_36;

import javax.swing.JOptionPane;

/**
 * Data: 17/11/2025
 * @author michael
 */
public class Ex_36 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que lê 7 quantidades (inteiro) e depois a média 
        dessas quantidades. O programa deve ainda imprimir elevado se a média 
        for superior a 100, médio se a média estiver entre 50 e 100, e baixo 
        se a média for inferior a 50.*/
        int quant[] = new int [7];
        for (int i=0; i<7; i++){
            quant[i]=Integer.parseInt(JOptionPane.showInputDialog("Insira a "
                    + "quantidade: "));
        }
        int soma = 0;
        for (int i=0; i<7; i++){
            soma = soma + quant[i];
        }
        float media = soma / 7f;
        JOptionPane.showMessageDialog(null, "A média das quantidades é: " 
                + media);
        if (media>100){
            JOptionPane.showMessageDialog(null, "Elevado");
        }
        else if (media>=50 && media<=100){
            JOptionPane.showMessageDialog(null, "Médio");
        }
        else {
            JOptionPane.showMessageDialog(null, "Baixo");
        }
    }
    
}
