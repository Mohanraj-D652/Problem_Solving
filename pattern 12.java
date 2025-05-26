
class main{

    public static void main(String[] args) {
        int n=5;
        
        for(int i=1; i<=n; i++){
            
            for(int j=1; j<=n-i; j++){
                System.out.print("  ");
            }
            for(int k=1; k<=2*i-1;k++){
                System.out.print("*"+' ');
            }
            System.out.println("");
        }
        for(int s=1; s<=n-1; s++){
            for(int l=1; l<=s; l++){
                System.out.print("  ");
            }
            for(int h=1; h<= 2*n - 2*s-1; h++){
                System.out.print("*"+" ");
            }
            System.out.println("");
        }
}
}