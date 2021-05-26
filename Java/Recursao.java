public class Recursao {
    
    public static void imprimir(String[] vetor, int indice ){

        if (indice == vetor.length - 1){
            System.out.println(vetor[indice]);
            return;
        }

        System.out.println(vetor[indice]);

        imprimir(vetor, indice + 1);
    }

    public static void main(String[] args) {        
        String vetor[] = {"Fulano 01", "Fulano 02", "Fulano 03", "Fulano 04"};        
        Recursao.imprimir(vetor, 0);
    }

}
