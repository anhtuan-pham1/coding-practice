# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# 1.2 CTCI
# runtime: O(nlogn) because default sorting algo in Python is Tim sort.
import unittest


def checkPermutation(s1: str, s2: str):

    if len(s1) != len(s2):
        return False

    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            print(False)
            return False
    print(True)
    return True


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("adasdas", "aadas", False),
        ("dog", "god", True),
        ("abcd", "bacd", True)
    )

    def test_cp(self):
        for str1, str2, expected in self.test_cases:
            assert checkPermutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
