/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_7;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author micha
 * Função: Exercícios iniciais
 */
public class Ex_7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        // exercício 7 - inteiro -1 e inteiro +1
        String n1;
        n1=JOptionPane.showInputDialog("Digite um número inteiro: ");
        int ant = Integer.parseInt(n1) - 1;
        int prox = Integer.parseInt(n1) + 1;
        JOptionPane.showMessageDialog(null, "<html>O inteiro anterior é " + ant
        + ". <br>O inteiro próximo é " + prox + ".");     
    }
    
}
