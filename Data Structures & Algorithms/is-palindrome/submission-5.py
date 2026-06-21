class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean data
        temp_list = list(s)
        alpha_num_list = []
        for i in temp_list:
            if i.isalnum():
                if i.isalpha():
                    alpha_num_list.append(i.lower())
                    continue    
                alpha_num_list.append(i)

        # edge case one len is palindorme 
        if len(alpha_num_list) == 1:
            return True
        #set LHS and RHS pointers
        LHS_ptr = None
        RHS_ptr = None
        if len(alpha_num_list) % 2 == 0:
            # 0 indexing
            LHS_ptr = int(len(alpha_num_list) / 2) - 1
            RHS_ptr = LHS_ptr + 1
        else: 
            LHS_ptr = int(math.floor(len(alpha_num_list) / 2)) - 1
            RHS_ptr = LHS_ptr + 2

        #iterate and comapre 
        for j in range(len(alpha_num_list)):
            print(LHS_ptr)
            print(LHS_ptr)
            #exit condition as lazy to write for loop range
            try:
                if alpha_num_list[LHS_ptr] != alpha_num_list[RHS_ptr]:
                    return False
                if LHS_ptr == 0 and RHS_ptr == len(alpha_num_list) - 1:
                    break
                LHS_ptr = LHS_ptr - 1
                RHS_ptr = RHS_ptr + 1
            except:
                #out of index one side longer than other
                return False
        return True;
        