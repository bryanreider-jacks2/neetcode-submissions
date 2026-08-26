class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = len(word)
            encoded_string += str(length) + "#" + word 

        return encoded_string
#               5#Hello5#World
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            i = j + 1
            decoded_strs.append(s[i:i + length])

            i += length
        return decoded_strs



        

