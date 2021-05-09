# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith "J 13
# Output: "Mr%20John%20Smith"
# CTCI: 1.3

def URLify(s: str):
    res = ''
    for i in s:
        if i == ' ':
            i = '%20'
        res = res + i

    print(res)
    return res


URLify("Mr John Smith")
