def merge_strings_two(word1:str, word2:str) -> str:
    new_str = ""

    index = 0
    while index < len(word1) or index < len(word2):
        if index <len(word1):
            new_str += word1[index]
        if index < len(word2):
            new_str += word2[index]
        
        index += 1
        
    return new_str


"Odd length number - n//2 - 1 digits are odd indices and the I should mix it "
x1 = "012345"
x2 = "13 024"

"----------------"

x = "012345"
y = "135024"
z = "304152"
n = 2

def encrypt(x,n):
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


def decrypt(x,n):

    odds = x[len(x)//2:]
    evens = x[:len(x)//2]

    for _ in range(n):
        x = merge_strings_two(odds,evens)

    return x

print(encrypt("12345", 1))

print(decrypt("24135", 1))