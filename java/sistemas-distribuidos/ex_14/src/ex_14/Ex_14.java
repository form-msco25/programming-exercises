/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_14;

import java.util.Scanner;

/**
 * Data: 14/11/2025
 * @author micha
 * Função: IF (ciclo condicional) na consola (terminal)
 */
public class Ex_14 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Crie um programa que peça ao utilizador o nome e o ano de nascimento. 
        O programa deve mostrar uma mensagem de boas vindas e depois mostrar 
        o pokerstar ou o canal panda. Caso a idade seja superior 
        ou inferior a 18.*/
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Insira o seu nome:");
        String nome = sc.nextLine();
        
        System.out.println("Insira o seu ano de nascimento:");
        int ano_nasc = sc.nextInt();
        
        int idade = 2025 - ano_nasc;
        
        if (idade>=18)
            System.out.print("Bem-vindo(a) ao Pokerstar \n");        
        else
            System.out.print("Bem-vindo(a) ao Canal Panda \n");                   
        
    }
    
}
