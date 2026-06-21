class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        
        if len(s_list) % 2 != 0:
            return False 
        
        # check if immediate closures all the way ()[] etc
        for i in range(1, len(s_list), 2): 
            if self.correct_lhs(s_list[i - 1]):
                break 
            if self.correct_rhs(s_list[i]):
                break
            if self.flip_rhs(s_list[i]) != s_list[i - 1]:
                break
            if  i == len(s_list) - 1:
                return True
        
        # check if palindrome
        lhs = int(len(s_list) / 2) - 1 
        rhs = lhs + 1
        try:
            for i in range(len(s_list)):
                if self.correct_lhs(s_list[lhs]):
                    return False
                if self.correct_rhs(s_list[rhs]):
                    return False
                if s_list[lhs] != self.flip_rhs(s_list[rhs]):
                    return False
                # exit
                if lhs == 0 and rhs == len(s_list) - 1:
                    break
                lhs -= 1
                rhs += 1
        except Exception as e: 
            return False
        
        return True

    def correct_lhs(self, s: str) -> bool:
        return s not in [ '(', '{', '[']

    def correct_rhs(self, s: str) -> bool:
        return s not in [ ')', '}', ']']

    def flip_rhs(self, s: str) -> str:
        if s == '}':
            return '{'
        elif s == ')':
            return '('
        else:
            return '['
  