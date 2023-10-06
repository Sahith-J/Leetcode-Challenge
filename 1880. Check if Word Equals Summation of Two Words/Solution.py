class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        s1=''
        s2=''
        s3=''
        for c in firstWord:
            s1+=str(ord(c)-ord('a'))
        for c in secondWord:
            s2+=str(ord(c)-ord('a'))
        for c in targetWord:
            s3+=str(ord(c)-ord('a'))
        return int(s1)+int(s2)==int(s3)
            
        
