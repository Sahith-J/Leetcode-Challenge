class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0

        for word in text.split(" "):
            check = True
            for char in brokenLetters:
                if char in word:
                    check = False
            
            if check:
                count += 1
        
        return count
        
