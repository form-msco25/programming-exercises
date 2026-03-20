/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_26;

import javax.swing.JOptionPane;

/**
 * Data: 10/11/2025
 * @author michael
 */
public class Ex_26 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Classe Formando
        /*  Pretende-se que implemente uma classe (formando) e coloque os 
        atributos (numero, nome, morada, cpostal, data_nascimento e sexo). 
        O programa deve permitir a leitura dos valores de toda a turma e depois 
        mostrar os valores impressos.*/

        class Formando{
            int num;
            String nom, mor, cpos, dataNas, sex;            
        }
        Formando f1 = new Formando();
        f1.num=Integer.parseInt(JOptionPane.showInputDialog(null, 
                "Qual o número?"));
        f1.nom=JOptionPane.showInputDialog(null, "Qual o seu nome?");
        f1.mor=JOptionPane.showInputDialog(null, "Qual a sua morada?");
        f1.cpos=JOptionPane.showInputDialog(null, "Qual o código postal?");
        f1.dataNas=JOptionPane.showInputDialog(null, "Qual a data "
                + "de nascimento?");
        f1.sex=JOptionPane.showInputDialog(null, "Qual o seu sexo?");
        JOptionPane.showMessageDialog(null, "<html>Olá " + f1.nom + 
                "<br>O seu número é: " + f1.num + "<br>O seu código "
                + "postal é: " + f1.cpos + "<br>Data de nascimento: " 
                + f1.dataNas + "<br>O seu sexo é: " + f1.sex);
    }
    
}
