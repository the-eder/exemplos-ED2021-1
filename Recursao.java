import java.lang.reflect.Array;
import java.util.LinkedList;

public class Recursao {

    private static int[] vetor2;

    public int soma_lista(LinkedList<Integer> numLista) {
        // Caso Básico
        if (numLista.size() == 1) {
            return numLista.pop();
        };

        // Mudança de Estado  + Chamada a si mesma
        return numLista.pop() + soma_lista(numLista);

    }

    public void imprimir_vetor(int[] vetor, int indice) {        
        // Caso Básico                
        if (indice == vetor.length - 1) {
            System.out.println(vetor[indice]);
            return;
        };                

        System.out.println(vetor[indice]);

        // Lei 3              Lei 2
        imprimir_vetor(vetor, indice + 1);
    }

    public static void main(String[] args) {
        Recursao recursao = new Recursao();
        LinkedList<Integer> numList = new LinkedList<Integer>();
        numList.add(1);
        numList.add(3);
        numList.add(5);
        numList.add(7);
        numList.add(9);
        System.out.println(recursao.soma_lista(numList));        
        int vetor[] = {1,3,5,7,9};        
        recursao.imprimir_vetor(vetor, 0);
    }
}