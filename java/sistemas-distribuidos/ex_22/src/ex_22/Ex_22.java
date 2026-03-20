/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex_22;

import javax.swing.JOptionPane;

/**
 *
 * @author michael
 * Função: Número maior
 */
public class Ex_22 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /* Considere-se o problema de ler três números e calcular o maior deles.
        Na resolução do problema deve ser adoptada uma estratégia de isolamento 
        dos vários casos, primeiro é testado o número A, depois o número B e 
        caso nenhum dos dois seja o máximo, por exclusão de partes, se conclui
        que o número C é o maior de todos. */
        int a = Integer.parseInt(JOptionPane.showInputDialog("Digite "
                + "o primeiro número: "));
        int b = Integer.parseInt(JOptionPane.showInputDialog("Digite "
                + "o segundo número: "));
        int c = Integer.parseInt(JOptionPane.showInputDialog("Digite "
                + "o terceiro número: "));
        
        int maior = 0;
        
        if (a>b && a>c){
            maior = a;
        }
        else{
            if (b>a && b>c){
                maior = b;
            }
            else{                
                maior = c;
            }
        }
        JOptionPane.showMessageDialog(null, "O número maior é " + maior);
    }
    
}
