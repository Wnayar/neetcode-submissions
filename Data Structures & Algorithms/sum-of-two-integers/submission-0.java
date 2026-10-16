class Solution {
    // tc O(1), max times we add is 32 since 32 bits 
    // sc O(1)
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b; 
            b = carry;
        }
        return a;    
    }
}
//    1
// 4   100
// 6   110
// 10 1010

// 1 1 -> 0 
// 0 0 -> 0 
// 1 0 -> 1
// xor handles 

// deal with carry lets say 1 and 1 i need to carry 1 to next position 
// 1 1 -> 1
// 0 0 -> 0
// 0 1 -> 0
// and operation then SLL 1 

// then take carry and add to result, then repeat till carry is 0 