# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)
# CTCI: 1.4
def palindromePermutation(s: str):
    freq = set()
    for i in s.split():
        for j in i:
            c = j.lower()
            if c in freq:
                freq.remove(c)
            else:
                freq.add(c)
    print(len(freq) <= 1)
    return len(freq) < 1


palindromePermutation("Tact Coa")
palindromePermutation("tact coa")
