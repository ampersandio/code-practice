word1 = "abc"
word2 = "pq"

def merge_strings(word1:str,word2:str) -> str:
    new_str = ""

    min_len = len(min(word1,word2, key=len))

    for i in range(min_len):
        new_str += word1[i]
        new_str += word2[i]

    new_str += max(word1,word2,key=len)[min_len::]

    return(new_str)

print(merge_strings(word1,word2))


# def merge_strings_two(word1:str, word2:str) -> str:
#     new_str = ""

#     index = 0
#     while index < len(word1) or index < len(word2):
#         if index <len(word1):
#             new_str += word1[index]
#         if index < len(word2):
#             new_str += word2[index]
        
#         index += 1
        
#     return new_str

# print(merge_strings_two(word1,word2))




def merge_strings(word1, word2):
    index = 0

    new_word = ""

    while index < len(word1) or index < len(word2):
        if len(word1) > index:
            new_word += word1[index]
        if len(word2) > index:
            new_word += word2[index]

        index += 1

    return new_word


print(merge_strings("penis", "vagina"))