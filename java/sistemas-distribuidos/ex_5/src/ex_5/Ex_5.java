/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_5;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author micha
 * Função: Exercícios iniciais
 */
public class Ex_5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        // exercício 5 - idade atual
        String ano_nasc, ano_atual;
        ano_nasc=JOptionPane.showInputDialog("Qual é o seu ano de nascimento?");
        ano_atual=JOptionPane.showInputDialog("Qual é o ano atual?");
        int idade = Integer.parseInt(ano_atual)+Integer.parseInt(ano_nasc);
        JOptionPane.showMessageDialog(null, "Tem" + idade + "anos.");       
    }
    
}
