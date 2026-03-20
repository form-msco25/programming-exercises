/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_17;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Clasificação de temperaturas
 */
public class Ex_17 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Coloque as condições necessárias para aparecer a palavra “FRIO” 
        se a média for inferior a 15, “AMENO” se a temperatura for superior a 15
        e inferior a 25, e “QUENTE” se a temperatura for superior a 25. */
        float temp1 = Float.parseFloat(JOptionPane.showInputDialog(null,"Insira"
                + " a primeira temperatuda:"));
        float temp2 = Float.parseFloat(JOptionPane.showInputDialog(null,"Insira"
                + " a segunda temperatuda:"));
        float temp3 = Float.parseFloat(JOptionPane.showInputDialog(null,"Insira"
                + " a terceira temperatuda:"));
        
        float media = (temp1 + temp2 + temp3) / 3;
        if (media < 15){
            JOptionPane.showMessageDialog(null, "<html>A temperatura media é " 
                    + media + ". <br>A condição é FRIO!");
        }
        else{
            if (media >= 15 && media < 25){
                JOptionPane.showMessageDialog(null, "<html>A temperatura media é " 
                + media + ". <br>A condição é AMENO!");
            }
            else{
                JOptionPane.showMessageDialog(null, "<html>A temperatura media é " 
                + media + ". <br>A condição é QUENTE!");
            }
        }

    }
    
}
