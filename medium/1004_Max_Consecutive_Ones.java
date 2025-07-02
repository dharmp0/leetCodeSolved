class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int longest = 0;

        while(right < nums.length){
            if(nums[right] == 1){
                right++;
            }
            else{
                k--;
                if(k >= 0){
                    right++;
                }
                else{
                    while(k < 0){
                        if(nums[left] == 0){
                            right++;
                            k++;
                        }
                        left++;
                    }
                }
            }
            if(longest < right - left){
                longest = right - left;
            }
        }
        return longest;
    }
}
