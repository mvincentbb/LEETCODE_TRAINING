package binarySearch;


public class BinarySearch {

    public int search(int[] nums, int target) {
        int high = nums.length -1 ;
        int low = 0;
        while (low <= high) {
            int mid = (low + high)/2;
            int guess = nums[mid];
            if(guess == target) return mid;
            else if (guess > target)high = mid -1 ;
            else low = mid +1 ;
        }
        return -1;
    }
    }

