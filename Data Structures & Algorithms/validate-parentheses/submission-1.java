class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> complement = new HashMap<>();

        complement.put('}', '{');
        complement.put(']', '[');
        complement.put(')', '(');

        Deque<Character> stack = new ArrayDeque<>();

        for(Character ch: s.toCharArray()) {
            if(complement.containsKey(ch)) {
                if (stack.size() == 0 || !stack.peek().equals(complement.get(ch)) ) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(ch);
            }
        }

        return stack.size() == 0;

    }
}
