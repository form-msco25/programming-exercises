/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_27;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_27 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Escreva uma classe (jogador) que contem os valores (numero, nome, 
        posição, data_nascimento, velocidade, ataque e defesa). O programa deve 
        ler os valores de uma equipa 11 jogadores e mostrar os resultados 
        impressos.*/
        class Jogador{
            int num, vel, ata, def;
            String nom, pos, dataNas;
        }
        Jogador j1 = new Jogador();
        j1.num=Integer.parseInt(JOptionPane.showInputDialog(null, 
                "Qual o número?"));
        j1.nom=JOptionPane.showInputDialog(null, "Qual o seu nome?");       
        j1.pos=JOptionPane.showInputDialog(null, "Qual a sua posição?");
        j1.dataNas=JOptionPane.showInputDialog(null, "Qual a data "
                + "de nascimento?");
        j1.vel=Integer.parseInt(JOptionPane.showInputDialog(null, "Qual a sua "
                + "velocidade?"));
        j1.ata=Integer.parseInt(JOptionPane.showInputDialog(null, "Qual o "
                + "seu ataque?"));        
        j1.def=Integer.parseInt(JOptionPane.showInputDialog(null, "Qual a "
                + "sua defesa?"));
        JOptionPane.showMessageDialog(null, "<html>Olá " + j1.nom + 
                "<br>O seu número é: " + j1.num + "<br>A sua posição é: "
                + j1.pos + "<br>Data de nascimento: " + j1.dataNas 
                + "<br>A sua velocidade é: " + j1.vel + "<br>O seu ataque é: "
                + j1.ata + "<br>A sua defesa é: " + j1.def);
    }
    
}
