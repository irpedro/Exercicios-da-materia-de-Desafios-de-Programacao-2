//Pedro Gabriel Ruiz - 13875571
//Matheus Silva Lopes da Costa - 12674680
//Mateus Caetano da Silva - 12543989

import java.util.Scanner;

public class Main {
    
    public static void linhaHifen () {
        System.out.printf("-");
    }

    public static void ultimaColuna(int coluna, int s) {

        if (coluna == s+2) {
            System.out.printf("|");
        }
        else {
            System.out.printf(" ");
        }
        
    }

    public static void imprimeLinha(int valor, int linha, int coluna, int s)
    {
        int inicio = 0;
        int meio = (2*s+3)/2;
        int fim = 2*s+2;

        switch (valor) {
            case 1:
                ultimaColuna(coluna, s);
                break;
        
            case 2:
                if ((linha < meio) && (coluna == s+2)) {
                    System.out.printf("|");
                }
                else if ((linha > meio) && (coluna == 1)) {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }

                break;

            case 3:
                ultimaColuna(coluna, s);
                break;
        
            case 4:
                if ((linha == meio) && (coluna != 1) && (coluna != s+2) && (coluna <= s+2)) {
                    System.out.printf("-");
                }
                else if ((linha < meio) && (coluna == 1) && (linha != 0))
                {
                    System.out.printf("|");
                }
                else{
                    ultimaColuna(coluna, s);
                }

                break;

            case 5:
                if ((linha > meio) && (coluna == s+2)) {
                    System.out.printf("|");
                }
                else if ((linha < meio) && (coluna == 1)) {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }
                break;
        
            case 6:
                if (coluna == 1) {
                    System.out.printf("|");
                }
                else if ((linha > meio) && (coluna == s+2))
                {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }
                break;

            case 7:

                if (linha == 0) {
                    System.out.printf("-");
                }
                else if ((coluna == s+2) && (linha != meio) && (linha != fim)) {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }
                break;
        
            case 8:
                if ((coluna == s+2) && (linha != 0)) {
                    System.out.printf("|");
                }
                else if ((coluna == 1) && (linha != 0))
                {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }
                break;
                
            case 9:
                if ((coluna == s+2) && (linha != 0)) {
                    System.out.printf("|");
                }
                else if ((linha < meio) && (coluna == 1) && (linha != 0))
                {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }

                break;

            default:
            //Zero

                if ((linha == inicio) || (linha == fim)) {
                    System.out.printf("-");
                }
                else if ((coluna == s+2) || (coluna == 1)) {
                    System.out.printf("|");
                }
                else {
                    System.out.printf(" ");
                }
                
                break;
        }
    }

    public static void main(String[] args)  {

        Scanner sc = new Scanner(System.in);
        while(true){

            int escala = sc.nextInt();
            int vet[] = new int[6];
            vet[0] = 2;
            vet[1] = 3;
            vet[2] = 5;
            vet[3] = 6;
            vet[4] = 8;
            vet[5] = 9;
            
            String numero = sc.next();     

            if (escala == 0) {
                break;
            }

            for (int i = 0; i < 2*escala+3; i++) {
                //Para cada linha
                for (int j = 0; j < numero.length(); j++) {
                    //Para cada número
                    for (int j2 = 1; j2 <= escala+2; j2++) {
                        //Para cada coluna
                        if (i % (escala+1) == 0) {
                            //Se for inicio ou meio ou fim
                            if ((j2 != escala+2) && (j2 != 1)) {
                                //Se não for o primeiro ou o último coluna
                                for (int k = 0; k < vet.length; k++) {
                                    int temp = Integer.parseInt(String.valueOf(numero.charAt(j)));
                                    if (temp == vet[k]) {
                                        //Se for 2, 3, 5, 6, 8 ou 9
                                        linhaHifen();
                                    }
                                    else if (temp == 4) {
                                        imprimeLinha(4, i, j2, escala);
                                        break;
                                    }
                                    else if (temp == 7) {
                                        imprimeLinha(7, i, j2, escala);
                                        break;
                                    }
                                    else if (temp == 0) {
                                        imprimeLinha(0, i, j2, escala);
                                        break;
                                    }
                                    if (temp == 1) {
                                        imprimeLinha(1, i, j2, escala);
                                        break;
                                    }
                                }
                            }
                            else
                            {
                                System.out.printf(" ");
                            }
                        }
                        else{
                            imprimeLinha(Integer.parseInt(String.valueOf(numero.charAt(j))), i, j2, escala);
                        }
                    }
                    System.out.printf(" ");
                }
                System.out.printf("\n");
            }
        }
        sc.close();
    }
}