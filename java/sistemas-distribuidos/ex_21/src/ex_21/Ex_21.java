/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_21;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Média Aprovado ou Reprovado
 */
public class Ex_21 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Implemente um programa que permite ler as notas de um aluno 
        nos 3 períodos letivos e calcular a média. Em função da média mostra 
        uma mensagem com o conteúdo "Aprovado" ou "Reprovado".
        Consideram-se notas positivas as notas iguais ou superiores a 9.5. */
        float n1 = Float.parseFloat(JOptionPane.showInputDialog("Digte a nota "
                + "do 1º período letivo"));
        float n2 = Float.parseFloat(JOptionPane.showInputDialog("Digte a nota "
                + "do 2º período letivo"));
        float n3 = Float.parseFloat(JOptionPane.showInputDialog("Digte a nota "
                + "do 3º período letivo"));
        
        float media = (n1 + n2 + n3) / 3;
        if (media >= 9.5){
            JOptionPane.showMessageDialog(null, "Aprovado");
        }
        else{
            JOptionPane.showMessageDialog(null, "Reprovado");
        }
        
    }
    
}
