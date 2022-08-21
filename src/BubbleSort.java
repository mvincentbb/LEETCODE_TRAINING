import java.util.Arrays;

public class BubbleSort {

    public static int[] SortArray(int[]Nums) {

        for (int i = 0; i < Nums.length - 1; i++) {
            for (int j = i + 1; j < Nums.length; j++) {
                if(Nums[i]> Nums[j]){
                    int temp = Nums[j];
                    Nums[j] = Nums[i];
                    Nums[i]= temp;
                }
            }
        }
        return Nums;

    }

    public static void main(String[] args) {
        int [] Nums = {0,20,1,18,2,6,4};
        System.out.println(Arrays.toString(SortArray(Nums)));
    }
}
