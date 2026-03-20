/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_24;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Classificação triângulo
 */
public class Ex_24 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Elabore um algoritmo que, após ler o tempo que determinada viatura 
        permaneceu estacionada no parque, indique a quantia que deve ser paga.
        Preços: 
        1ª hora = 1€
        2ª hora = 0,8 € 
        A partir da 2a hora: 0,40 €/hora
        Ex.: Uma viatura que esteve estacionada 2 horas e 30 minutos. 
        Deve pagar 2 € (1 hora x 1€ + 1 hora x 0,8 € + 0,5 hora x 0,4 € )*/
        float h = Float.parseFloat(JOptionPane.showInputDialog("Digite o número "
                + "de horas. "));
        
        float valor;
        if (h<=1){
            valor = 1.0f;
            JOptionPane.showMessageDialog(null, "Valor a pagar: " + valor 
                    + "€.");
        }
        else if (h<=2){
            valor = 1.0f + 0.8f;
            JOptionPane.showMessageDialog(null, "Valor a pagar: " + valor 
                    + "€.");
        }
        else{
            valor = 1.0f + 0.8f + ((h-2)*0.4f);
            JOptionPane.showMessageDialog(null, "Valor a pagar: " + valor 
                    + "€.");
        }
    }
    
}
