'''
Reverse Words in a String

Input: s = "the sky is blue"
Output: "blue is sky the"

'''
s = "a good   example"

class Solution:
    '''
    No builtins used.
    '''
    def reverseWords(self, s: str) -> str:
        new_string = []
        chunk = ""

        for i in range(len(s)):
            if s[i].isalnum():
                chunk += s[i]

            elif s[i] == " " and chunk:
                if chunk[-1] != " ":
                    new_string.insert(0,chunk)
                    chunk = ""

        if chunk:
            new_string.insert(0,chunk)

        return " ".join(new_string)
    
    def reverseWords2(sef, s:str) -> str:
        return " ".join(s.split()[::-1])


test = Solution()

print(test.reverseWords2(s))
