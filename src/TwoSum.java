import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
        public static int[] twoSum(int[] nums, int target) {
            int diff = 0;
            int arrayInt[] = new int[2];
            for(int i = 0; i < nums.length; i++){
                    diff = target - nums[i];
                    for ( int j =  i + 1 ; j< nums.length ; j++) {
                        if(nums[j] == diff){
                             arrayInt = new int[]{nums[i], nums[j]};
                            return arrayInt;
                        }
                    }
            }
            return arrayInt;
        }

        public static int[] Sum(int[] nums, int target){
            Map<Integer, Integer>taMap = new HashMap<>();
            int [] arr = new int[2];
            for(int i =0; i< nums.length; i++){
                int diff = target - nums[i];
                if(taMap.containsKey(diff)){
                    arr = new int[]{i, taMap.get(diff)};
                    return arr;
                }
                    taMap.put(nums[i],i);
            }
            return arr;
        }

    public static int[] twoSumBest(int[] numbers, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            if (map.containsKey(target - numbers[i])) {
                result[1] = i;
                result[0] = map.get(target - numbers[i]);
                return result;
            }
            map.put(numbers[i], i);
        }
        return result;
    }


    public static void main(String[] args) {
        int [] nums = {3,2,4};
        int target = 6;
//        System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.toString(twoSumBest(nums, target)));

    }

}
