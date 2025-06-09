class main{
    public static void main(String[] args) {
        int count=0;
        int n=12345;
        while(n>0){

            count=count+1;
            int id=n%10;
            n=n/10;
            System.out.println(id);
        //
        

        }
        System.out.println("Total count is: "+count);


    }
}
