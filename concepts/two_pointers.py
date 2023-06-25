def two_pointers_palindrome(s:str) -> bool:

    l = 0
    r = len(s)-1

    anagram = True

    while l <= r:
        if s[l] != s[r]:
            anagram = False

        l += 1
        r -= 1

    return(anagram)

