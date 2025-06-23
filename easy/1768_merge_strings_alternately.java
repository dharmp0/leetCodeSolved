class Solution {
    public String mergeAlternately(String word1, String word2) {
        
        StringBuilder result = new StringBuilder();
        
        int max_length = word1.length() > word2.length() ? word1.length() : word2.length();
        
        for(int i = 0; i < max_length; i++){
            if(i < word1.length()) {
                result.append(word1.charAt(i));
            }
            if (i < word2.length()) {
                result.append(word2.charAt(i));
            }
        }

        return result.toString();
    }
}
