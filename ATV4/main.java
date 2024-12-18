import java.util.Scanner;

public class main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

    	while(sc.hasNext())
    	{

			int[][] garrafas = new int[3][3];

			for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    garrafas[i][j] = sc.nextInt();
                }
            }

			/*
			BCG
			BGC
			CBG
			CGB
			GBC
			GCB	
			 */

    		int bcg = garrafas[0][1] + garrafas[0][2] + garrafas[1][0] + 
					  		garrafas[1][1] + garrafas[2][0] + garrafas[2][2];


    		int bgc = garrafas[0][1] + garrafas[0][2] + garrafas[1][0] + 
							garrafas[1][2] + garrafas[2][0] + garrafas[2][1];

    		
    		int cbg = garrafas[0][1] + garrafas[0][0] + garrafas[1][2] + 
							garrafas[1][1] + garrafas[2][2] + garrafas[2][0];


    		int cgb = garrafas[0][1] + garrafas[0][0] + garrafas[1][2] + 
							garrafas[1][0] + garrafas[2][2] + garrafas[2][1];

    		
    		int gbc = garrafas[0][0] + garrafas[0][2] + garrafas[1][1] + 
							garrafas[1][2] + garrafas[2][1] + garrafas[2][0];


    		int gcb = garrafas[0][0] + garrafas[0][2] + garrafas[1][1] + 
							garrafas[1][0] + garrafas[2][1] + garrafas[2][2];

    		
    		int totalColuna1 = Math.min(bgc, bcg);
    		int totalColuna2 = Math.min(cgb, cbg);
    		int totalColuna3 = Math.min(gcb, gbc);

    		int Total = Math.min(totalColuna1, Math.min(totalColuna2, totalColuna3));
			
    		if(Total == bcg)
    			System.out.println("BCG " + Total);
			else if(Total == bgc)
					System.out.println("BGC " + Total);
				else if(Total  == cbg)
						System.out.println("CBG " + Total);
					else if(Total  == cgb)
							System.out.println("CGB " + Total);
						else if(Total  == gbc)
								System.out.println("GBC " + Total);
							else if(Total  == gcb)
									System.out.println("GCB " + Total);
    	}
		sc.close();
   }
}