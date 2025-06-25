class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
        Set<Integer> set1 = new HashSet<>();
        for(int num: nums1) set1.add(num);

        Set<Integer> set2 = new HashSet<>();
        for(int num: nums2) set2.add(num);

        Set<Integer> set1_only = new HashSet<>(set1);
        Set<Integer> set2_only = new HashSet<>(set2);

        set1_only.removeAll(set2);
        set2_only.removeAll(set1);

        List<List<Integer>> result = new ArrayList<>();

        result.add(new ArrayList<>(set1_only));
        result.add(new ArrayList<>(set2_only));

        return result;

    }
}
