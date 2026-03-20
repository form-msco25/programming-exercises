/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_8;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Exercícios de reforço
 */
public class Ex_8 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String nome;
        String morada;
        int idade;
        
        nome=JOptionPane.showInputDialog(null,"Qual o seu nome?");
        morada=JOptionPane.showInputDialog(null,"Qual a sua morada?");
        idade=Integer.parseInt(JOptionPane.showInputDialog(null,
                "Qual a sua idade?"));
        JOptionPane.showMessageDialog(null, "Olá " + nome);
        JOptionPane.showMessageDialog(null, "Moras em " + morada);
        int ano = 2025-idade;
        JOptionPane.showMessageDialog(null, "Nasceste em " + ano);
    }    
}
