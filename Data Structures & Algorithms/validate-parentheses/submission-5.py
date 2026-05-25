class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_symbols = {'(': ')', '{': '}', '[': ']'}
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif len(stack)>0:
                last_c = dict_symbols.get(stack.pop())
                if ch != last_c:
                    return False
            else:
                return False
        return len(stack) == 0

