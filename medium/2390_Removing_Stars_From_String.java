class Solution {
    public String removeStars(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '*')
                stack.pop();
            
            else
                stack.push(c);
        }
        StringBuilder result = new StringBuilder();
        for (char c: stack){
            result.append(c);
        }
        result.reverse();
        return result.toString();
    }
}
