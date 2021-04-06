import java.util.HashMap;

class Solution {

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] test = TwoSum(nums, target);
        for (int i = 0; i < test.length; i++){
            System.out.println(test[i]);
        }
        
    }
    public static int[] TwoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap <Integer,Integer> map = new HashMap <Integer, Integer>();
        for (int i =0; i < nums.length; i++){
            int expectedNum = target - nums[i];
            if (map.containsKey(expectedNum)){
                result[0] = map.get(expectedNum);
                result[1] = i;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}