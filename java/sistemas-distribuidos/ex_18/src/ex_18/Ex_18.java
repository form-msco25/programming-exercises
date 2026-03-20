/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_18;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Clasificação de temperaturas
 */
public class Ex_18 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* O índice de massa corporal (IMC) de um indivíduo é obtido 
        dividindo-se o seu peso (em Kg) pela sua altura (em m) ao quadrado. 
        Escreva um programa que solicite ao utilizador o fornecimento do seu 
        peso em kg e de sua altura em m e a partir deles calcule o índice de 
        massa corporal do utilizador. Deve ainda indicar um dos valores:
        -Até 18.5 (inclusive): abaixo do peso normal
        -De 18.5 a 25 (inclusive): peso normal
        -De 25 a 30 (inclusive): acima do peso normal
        -Acima de 30: obesidade. */
        float peso = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira"
                + " o seu peso em kg:"));
        float altura = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira"
                + " a sua altura em m:"));       
        float imc = peso / (altura * altura);
        
        if (imc <= 18.5){
            JOptionPane.showMessageDialog(null,"O seu IMC é " + imc, 
                    ". Está abaixo do peso normal.", JOptionPane.ERROR_MESSAGE);
        }
        else{
            if (imc > 18.5 && imc <= 25){
                JOptionPane.showMessageDialog(null,"O seu IMC é " + imc, 
                    ". O seu peso é normal.",
                    JOptionPane.INFORMATION_MESSAGE);
            }
            else{
                if (imc > 25 && imc <= 30){
                    JOptionPane.showMessageDialog(null,"O seu IMC é " + imc, 
                        ". Está acima do peso normal.",
                        JOptionPane.INFORMATION_MESSAGE);               
                }
                else{
                    JOptionPane.showMessageDialog(null,"O seu IMC é " + imc, 
                        ". Está obeso.",
                        JOptionPane.ERROR_MESSAGE);
                }
            }
        }
        
    }
    
}
