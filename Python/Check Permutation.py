#Check Permutation: Given two strings, write a method to decide if one is a permutation of the
#other.
#1.2 CTCI
#runtime: O(nlogn) because default sorting algo in Python is Tim sort.

def checkPermutation (s1:str, s2:str):

    if len(s1)!= len(s2):
        return False

    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    for i in range (0,len(s1)):
        if s1[i] != s2[i]:
            print(False)
            return False
    print(True)
    return True

#False
checkPermutation("dbcahdkjsad","dasdsa")

