/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_9;

import javax.swing.JOptionPane;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: Exercícios de reforço
 */
public class Ex_9 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador o número de quilómetros 
        e os litros de gasolina gastos.
        O programa deve mostrar o consumo médio.*/
        String kms;
        String litros;
        
        kms=JOptionPane.showInputDialog(null,"Digite os kilómetros percorridos?");
        litros=JOptionPane.showInputDialog(null,"Digite os litros de gasolina gastos?");
        float consumo = (Float.parseFloat(litros) / Float.parseFloat(kms)) * 100;
        JOptionPane.showMessageDialog(null, "Consumo médio = "
                + consumo);
    }    
}
