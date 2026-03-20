/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_25;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_25 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /*  Pretende-se que implemente o código acima com os seu valores.*/

        class Conta {
            int numero;
            String nome;
            double saldo;
            double limite;
        }
        Conta minhaconta;
        minhaconta = new Conta();
        minhaconta.nome = "Michael Ortiz";
        minhaconta.saldo = 1500;
        minhaconta.limite = 20000;
        System.out.println("Bem-vindo " + minhaconta.nome + ". A conta nº " 
                + minhaconta.numero + " tem um saldo de " + minhaconta.saldo 
                + " e um limite de " + minhaconta.limite);
    }
    
}
