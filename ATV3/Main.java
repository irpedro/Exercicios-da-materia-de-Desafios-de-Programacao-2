import java.util.ArrayList;

class Main
{

    static int findGreatValue(int[][] garrafas, ArrayList<Integer> list, int maxValue) {
        int max = 0;
        for (int i = 0; i < 9; i++) {
            if ((garrafas[1][i] > max) && (garrafas[1][i] < maxValue)) {
                max = garrafas[1][i];
            }
        }

        for (int i = 0; i < 9; i++) {
            if (garrafas[1][i] == max) {
                list.add(i);
            }
        }
        maxValue = max;
        return maxValue;
    }

    static int countMoves(int[][] garrafas, ArrayList<Integer> list, int moves, int maxValue, boolean[] visited) {
        int container = 0;
        int temp = 0;

        for (int i = 8; i >= 0; i--) {
            if (maxValue == garrafas[1][i]) {
                if (i > 5){
                    if (visited[2] == false) {
                        temp += garrafas[1][i-3];
                        temp += garrafas[1][i-6];
                        container = 2;
                    }
                    continue;
                }
                else if (i > 2) {
                    if (visited[1] == false) {
                        temp += garrafas[1][i-3];
                        temp += garrafas[1][i+3];
                        container = 1;
                    }
                    continue;
                }
                else{
                    if (visited[0] == false) {
                        temp += garrafas[1][i+3];
                        temp += garrafas[1][i+6];
                        container = 0;
                    }   
                }
                break;
            }
            if (temp > moves) {
                moves = temp;
                visited[container] = true;
            }
            temp = 0;
        }
        
        System.out.println("Numero de movimentos: " + moves);
        return moves;
    }

    public static void main (String args[])  // entry point from OS
    {
        boolean[] visited = new boolean[3];

        int maxValue = 999999999;
        for (int i = 0; i < 3; i++) {
            //long maxValue = 2147483648L;


            int[][] garrafas = {{0, 1, 2, 0, 1, 2, 0, 1, 2},
                                {5, 10, 5 ,20 ,10 ,5 ,10, 20, 10}};

            
            ArrayList<Integer> list = new ArrayList<>();

            maxValue = findGreatValue(garrafas, list, maxValue);

            for (int index = 0; index < list.size(); index++) {
                System.out.println("Garrafa " + list.get(index) + " tem o maior valor");
            }

            int moves = 0;
            moves += countMoves(garrafas, list, moves, maxValue, visited);
            list.clear();
        }
    }
}
