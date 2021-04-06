# https://binarysearch.com/problems/Palindromic-Anagram

def solve( s):
    checked_dict = dict()
    ele_list = []
    for i in s:
        if i not in checked_dict.keys():
            checked_dict[i] = 1 
        else:
            checked_dict[i] +=1
    counter = 0
    for i in checked_dict.keys():
        if checked_dict[i] % 2 != 0:
            counter +=1 
            if counter >1 :
                return False
    return True


# Possible more optimal solution from Khoa
    # def solve(self, s):
    #     ele_list = dict()
    #     for i in s:
    #         if i in ele_list:
    #             del ele_list[i]
    #         else:
    #             ele_list[i] = 0
    #     return len(ele_list.keys()) < 2