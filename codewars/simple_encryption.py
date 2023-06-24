
def merge_strings_two(word1:str, word2:str) -> str:

    new_str = ""

    index = 0
    while index < len(word1) or index < len(word2):
        if index < len(word1):
            new_str += word1[index]
        if index < len(word2):
            new_str += word2[index]
        
        index += 1
        
    return new_str

def encrypt(x:str, n:int) -> str:
    odds = ""
    evens = ""

    for _ in range(n):

        for i,j in enumerate(x):
            if i % 2 == 0:
                evens += str(j)
            else:
                odds += str(j)

        x = (odds + evens)
        odds = ""
        evens = ""

    return x

def decrypt(x:str,n:int) -> str:

    while n > 0:
        odds = x[len(x)//2:]
        evens = x[:len(x)//2]
        x = merge_strings_two(odds,evens)
        n -= 1

    return x

encrypted = (encrypt("1234", 3))
print(encrypted)

decrypted = (decrypt(encrypted, 3))
print(decrypted)