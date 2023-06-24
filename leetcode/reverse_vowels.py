"Reverse Only Vowels in a String - Two pointers approach"

def reverseVowels(self, word: str) -> str:
    word = list(word)
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    l = 0
    r = len(word)-1 

    while l < r:
        if word[l] in vowels and word[r] in vowels:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        if word[l] not in vowels:
            l += 1
        elif word[r] not in vowels:
            r -= 1

    return "".join(word) 
