#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures? 
#1.1 CTCI
#runtime O(n^2)

# def isUnique (s:str):
#     char = ''
#     for i in s:
#         char = i
#         s = s[1:]
#         for j in s:
#             if i == j:
#                 print(False)
#                 return False
#     print(True)
#     return True


def isUnique (s:str):
    temp = ''.join(sorted(s))

    for i in range (0, len(temp) - 1):
        if temp[i] == temp[i+1]:
            print(False)
            return False
    print(True)
    return True


isUnique('aaaa') #False
isUnique('abcd') #True
isUnique('abad') #False
isUnique('adcc') #False

