class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        complement = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in (')', ']', '}'):
                if not stack or stack[-1] != complement[ch]:
                    return False
                stack.pop()
            elif ch in ('(', '[', '{'):
                stack.append(ch)

        return len(stack) == 0
                