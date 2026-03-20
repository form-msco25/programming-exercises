/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_33;

import javax.swing.JOptionPane;

/**
 * Data: 17/11/2025
 * @author michael
 */
public class Ex_33 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Faça um programa que lê 10 temperaturas (valores inteiros) 
        e depois as imprime. */
        int tam = 10; //tamanho do vetor
        int temp[] = new int[tam]; //declaração do vetor
        int i;
        //para ler os dados
        for (i=0; i<10; i++){
            temp[i]=Integer.parseInt(JOptionPane.showInputDialog(null, 
                    "Qual a temperatura " + (i+1) + "?: "));
        }        
        String msg = "<html>AS TEMPERATURAS SÃO:<br>";        
        //para imprimir os dados
        for (i=0; i<10; i++){
            msg = msg + "A temperatura " + (i+1) + " --> " + temp[i] 
                    + "<br>";
            JOptionPane.showMessageDialog(null, msg);
        }       
    }  
}
