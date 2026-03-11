class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = []
    
        num &= 0xffffffff
        
        while num:
            digit = num & 15        
            result.append(hex_chars[digit])
            num >>= 4                
        
        return "".join(reversed(result))
