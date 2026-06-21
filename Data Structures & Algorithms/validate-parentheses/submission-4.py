class Solution:
    def isValid(self, s: str) -> bool:
        # current if close type must match most recent
        close = {")" : "(", "]" : "[","}" : "{"}
        stack = []

        for c in s:
            if stack and c in close:
                if close[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        
        return not stack
            
