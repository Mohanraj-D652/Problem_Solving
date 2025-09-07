import java.util.Arrays;


public class Sort0s1s2s {
    public static void main(String[] args) {

        int[] arr = {0, 1, 2, 0, 1, 2};

        int zero = 0;
        int one = 0;
        int two = 0;
                
        for(int i =  0; i < arr.length; i++){
                    
            if(arr[i] == 0){
                zero += 1;
                        
            }
            else if(arr[i] == 1){
                one += 1;
                    
            }
            else{
                two += 1;
                }
                }
                
        for(int j = 0; j < zero; j++){
            arr[j] = 0;
                    
            }
        for(int j = zero; j < zero + one; j++){
            arr[j] = 1;
                    
            }
        for(int j = one + zero; j < arr.length; j++){
            arr[j] = 2;
            }
        System.out.println(Arrays.toString(arr));
    }
}