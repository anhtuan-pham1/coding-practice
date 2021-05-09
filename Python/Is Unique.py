# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# 1.1 CTCI

# runtime O(n^2)
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

# runtime O(nlogn)
import unittest


def isUnique(s: str):
    temp = ''.join(sorted(s))

    for i in range(0, len(temp) - 1):
        if temp[i] == temp[i+1]:
            print(False)
            return False
    print(True)
    return True


class Test(unittest.TestCase):
    test_cases = (
        ("aaaa", False),
        ("abcd",  True),
        ("abad",  False),
        ('adcc', False)
    )

    def test_unique(self):
        for s, expected in self.test_cases:
            assert isUnique(s) == expected


if __name__ == "__main__":
    unittest.main()
