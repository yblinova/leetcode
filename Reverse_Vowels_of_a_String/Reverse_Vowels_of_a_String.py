class Solution:      
    def reverseVowels(self, s: str) -> str:
        j = 0
        vowel = [0] * len(s)
        s = list(s)
    
        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or
            s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or
            s[i] == 'o' or s[i] == 'O' or s[i] == 'u' or s[i] == 'U'):
                vowel[j] = s[i]
                j += 1
    
        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or
            s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or
            s[i] == 'o' or s[i] == 'O' or s[i] == 'u' or s[i] == 'U'):
                j -= 1
                s[i] = vowel[j]
    
        return ''.join(s)